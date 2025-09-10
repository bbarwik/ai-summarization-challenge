"""Review the report and provide improvement suggestions."""

from ai_pipeline_core import (
    AIMessages,
    DocumentList,
    ModelName,
    PromptManager,
    get_pipeline_logger,
    llm,
    pipeline_task,
)

from ai_summarization.documents.flow import DraftDocument, PlanDocument, ReviewDocument

prompt_manager = PromptManager(__file__)
logger = get_pipeline_logger(__name__)


@pipeline_task
async def review_report(
    input_documents: DocumentList,
    plan_document: PlanDocument,
    draft_document: DraftDocument,
    model: ModelName,
    task_description: str,
) -> ReviewDocument:
    """Review the draft report and provide improvement suggestions."""
    prompt = prompt_manager.get(
        "review_report",
        task_description=task_description,
    )

    # Static context with input documents for caching
    context = AIMessages(input_documents)

    # Dynamic message with the prompt
    messages = AIMessages([plan_document, draft_document, prompt])

    result = await llm.generate(
        model=model,
        context=context,
        messages=messages,
    )

    return ReviewDocument.create(
        name=ReviewDocument.FILES.REPORT_REVIEW,
        content=result.content,
    )
