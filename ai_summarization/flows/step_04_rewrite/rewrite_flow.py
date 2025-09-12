"""Rewrite flow for final report generation."""

from ai_pipeline_core import DocumentList, FlowConfig, pipeline_flow

from ai_summarization.documents.flow import (
    DraftDocument,
    InputDocument,
    OutputDocument,
    PlanDocument,
    ReviewDocument,
)
from ai_summarization.flow_options import ProjectFlowOptions

from .tasks import rewrite_report


class RewriteFlowConfig(FlowConfig):
    """Configuration for rewrite flow."""

    INPUT_DOCUMENT_TYPES = [InputDocument, PlanDocument, DraftDocument, ReviewDocument]
    OUTPUT_DOCUMENT_TYPE = OutputDocument


@pipeline_flow(config=RewriteFlowConfig)
async def rewrite_flow(
    project_name: str,
    documents: DocumentList,
    flow_options: ProjectFlowOptions,
) -> DocumentList:
    """Rewrite the report incorporating review feedback."""
    # Get required documents
    input_docs = documents.filter_by(InputDocument)
    plan_doc = documents.get_by(PlanDocument)
    draft_doc = documents.get_by(DraftDocument)
    review_doc = documents.get_by(ReviewDocument)

    # Rewrite the report
    output_doc = await rewrite_report(
        input_documents=input_docs,
        plan_document=plan_doc,
        draft_document=draft_doc,
        review_document=review_doc,
        model=flow_options.core_model,
        task_description=flow_options.task_description,
    )

    # Return validated output
    return RewriteFlowConfig.create_and_validate_output([output_doc])
