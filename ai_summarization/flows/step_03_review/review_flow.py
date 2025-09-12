"""Review flow for report improvement."""

from ai_pipeline_core import DocumentList, FlowConfig, pipeline_flow

from ai_summarization.documents.flow import (
    DraftDocument,
    InputDocument,
    PlanDocument,
    ReviewDocument,
)
from ai_summarization.flow_options import ProjectFlowOptions

from .tasks import review_report


class ReviewFlowConfig(FlowConfig):
    """Configuration for review flow."""

    INPUT_DOCUMENT_TYPES = [InputDocument, PlanDocument, DraftDocument]
    OUTPUT_DOCUMENT_TYPE = ReviewDocument


@pipeline_flow(config=ReviewFlowConfig)
async def review_flow(
    project_name: str,
    documents: DocumentList,
    flow_options: ProjectFlowOptions,
) -> DocumentList:
    """Review the draft report and provide improvement suggestions."""
    # Get required documents
    input_docs = documents.filter_by(InputDocument)
    plan_doc = documents.get_by(PlanDocument)
    draft_doc = documents.get_by(DraftDocument)

    # Review the draft
    review_doc = await review_report(
        input_documents=input_docs,
        plan_document=plan_doc,
        draft_document=draft_doc,
        model=flow_options.core_model,
        task_description=flow_options.task_description,
    )

    # Return validated output
    return ReviewFlowConfig.create_and_validate_output([review_doc])
