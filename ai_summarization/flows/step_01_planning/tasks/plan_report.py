"""Plan the report structure and approach."""

from ai_pipeline_core import (
    AIMessages,
    DocumentList,
    ModelName,
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
    documents: DocumentList,
    model: ModelName,
    task_description: str,
) -> PlanDocument:
    """Create a detailed plan for the report based on input documents."""
    prompt = prompt_manager.get(
        "plan_report",
        task_description=task_description,
    )

    # Static context with input documents for caching
    context = AIMessages(documents)

    # Dynamic message with the prompt
    messages = AIMessages([prompt])

    result = await llm.generate(
        model=model,
        context=context,
        messages=messages,
    )

    return PlanDocument.create(
        name=PlanDocument.FILES.REPORT_PLAN,
        content=result.content,
    )
