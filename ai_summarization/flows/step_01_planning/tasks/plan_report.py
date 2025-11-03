"""Plan the report structure and approach."""

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

from ai_summarization.documents.flow import PlanDocument

prompt_manager = PromptManager(__file__)
logger = get_pipeline_logger(__name__)


@pipeline_task
async def plan_report(
    input_documents: DocumentList,
    model: ModelName,
) -> PlanDocument:
    """Create a detailed plan for the report based on input documents."""
    prompt = prompt_manager.get(
        "plan_report",
    )

    # Static context with input documents for caching
    context = AIMessages(input_documents)

    # Dynamic message with the prompt
    messages = AIMessages([prompt])

    result = await llm.generate(
        model=model,
        context=context,
        messages=messages,
        options=ModelOptions(
            reasoning_effort="high",
        ),
    )

    return PlanDocument.create(
        name=PlanDocument.FILES.REPORT_PLAN,
        content=result.content,
    )
