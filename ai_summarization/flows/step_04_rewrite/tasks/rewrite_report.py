"""Rewrite the report based on review feedback."""

from ai_pipeline_core import (
    AIMessages,
    DocumentList,
    ModelName,
    ModelOptions,
    PromptManager,
    get_pipeline_logger,
    llm,
    pipeline_task,
)

from ai_summarization.documents.flow import (
    DraftDocument,
    OutputDocument,
    PlanDocument,
    ReviewDocument,
)

prompt_manager = PromptManager(__file__)
logger = get_pipeline_logger(__name__)


@pipeline_task
async def rewrite_report(
    input_documents: DocumentList,
    plan_document: PlanDocument,
    draft_document: DraftDocument,
    review_document: ReviewDocument,
    model: ModelName,
) -> OutputDocument:
    """Rewrite the report incorporating review feedback."""
    prompt = prompt_manager.get(
        "rewrite_report",
    )

    # Static context with input documents for caching
    context = AIMessages(input_documents)

    # Dynamic message with the prompt
    messages = AIMessages([plan_document, draft_document, review_document, prompt])

    result = await llm.generate(
        model=model,
        context=context,
        messages=messages,
        options=ModelOptions(
            reasoning_effort="high",
        ),
    )

    return OutputDocument.create(
        name=OutputDocument.FILES.FINAL_REPORT,
        content=result.content,
    )
