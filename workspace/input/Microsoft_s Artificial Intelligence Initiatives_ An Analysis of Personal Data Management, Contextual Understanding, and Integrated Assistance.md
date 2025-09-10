# **Microsoft's Artificial Intelligence Initiatives: An Analysis of Personal Data Management, Contextual Understanding, and Integrated Assistance (2023-2025)**

# **1. Introduction**

The period between early 2023 and May 2025 has marked a transformative phase for Microsoft, characterized by an accelerated integration of Artificial Intelligence (AI) across its product ecosystem. This report conducts a comprehensive analysis of Microsoft's AI initiatives, with a specific focus on products and technologies pertaining to personal data management, contextual understanding, AI-driven assistance integrated into its operating systems and productivity suites, and the burgeoning capabilities of local AI processing. The objective is to dissect the evolution, core functionalities, underlying technologies, and critically, the privacy and data handling paradigms of Microsoft's key AI endeavors. Microsoft's overarching AI strategy aims to empower individuals and organizations by embedding intelligent capabilities into the tools they use daily. This involves leveraging large language models (LLMs), proprietary AI research, and a growing emphasis on on-device processing through specialized hardware. This analysis will investigate flagship initiatives such as Windows Copilot and its OS-level integration, Microsoft 365 Copilot within the productivity suite, the controversial Microsoft Recall feature, AI advancements in the Edge browser, and the versatile Microsoft Copilot Studio for custom AI development. Each initiative will be examined for its approach to user data, the balance between local and cloud processing, and its alignment with Microsoft's Responsible AI principles.

# **2. Overall Microso AI Strategy (2023-2025)**

Microsoft's mission in the generative AI era is to "empower every person and every organization on the planet to achieve more". <sup>1</sup> This mission translates into a strategy focused on integrating AI as a general-purpose technology, accessible and beneficial to a global audience. <sup>1</sup> A cornerstone of this strategy is a profound commitment to **Responsible AI**, emphasizing that for broad social acceptance, AI must be ethical, fair, safe, create new opportunities, and respect individual values and local resources.<sup>1</sup> Microsoft actively promotes dialogue around AI policy and governance, recognizing the importance of diverse voices and cultural context in AI development and deployment. 2

A significant thrust of Microsoft's AI strategy revolves around the concept of AI agents

redefining operations by automating, optimizing, and scaling innovation. $3$  These agents are envisioned as personal assistants, grounded in user work content, designed to augment human capacity rather than replace it. $3$  This vision is materializing through offerings like Microsoft 365 Copilot, positioned as the "user interface for AI".<sup>3</sup> The company is also fostering an ecosystem for AI development through initiatives like the Microsoft AI Cloud Partner **Program**<sup>3</sup> and platforms such as **Azure AI Foundry**. Azure AI Foundry aims to simplify development and accelerate the path to production for AI applications, providing tools, infrastructure, and access to open and cutting-edge models.<sup>3</sup> This platform is already utilized by a significant number of customers, indicating a push towards more mature AI implementations.<sup>3</sup> Microsoft's strategy also involves enabling partners to build and grow their AI practices, recognizing that AI-driven projects are a significant growth area.<sup>3</sup>

# **3. Key Products and Initiatives**

# **3.1. Windows Copilot & OS-Level AI Integration**

# **Product Overview & Evolution**

Windows Copilot was formally introduced as an AI assistant integrated into Windows 11, succeeding the discontinued Cortana.<sup>4</sup> Plans to integrate Copilot directly into the Windows 11 taskbar were announced at Microsoft's Build 2023 conference.<sup>4</sup> By early 2024, a dedicated Copilot key was announced for Windows keyboards, signaling a deeper hardware-software integration.<sup>4</sup> Initially accessible as a web-based application or sidebar, an update in April 2025 fully integrated Copilot as a local application for both Windows 11 and Windows 10 (version 19041.0 or later), aiming for improved performance and reduced memory usage.<sup>5</sup> This evolution underscores a shift towards a more embedded and responsive AI experience within the operating system. The introduction of Copilot + PCs in 2024, specifically designed for AI with powerful Neural Processing Units (NPUs), further marked a significant step in this evolution, enabling more advanced on-device AI capabilities. 6

The proliferation of the "Copilot" brand across numerous Microsoft products—Windows Copilot, Microsoft 365 Copilot, Copilot in Edge, Copilot Studio, and various specialized Copilots—while indicating a unified AI strategy, presents a potential challenge for users. Distinguishing the precise capabilities, data access mechanisms, and privacy implications of each specific "Copilot" instance can become complex. For example, Windows Copilot interacting with local files operates under different data governance than Microsoft 365 Copilot accessing enterprise data via Microsoft Graph. This necessitates clear communication from Microsoft and careful attention from users and administrators to understand the context of each Copilot interaction.

# **Core Features & Functionalities**

Windows Copilot aims to provide AI-driven assistance directly within the operating system. Its functionalities include:

- **Information Retrieval and Summarization:** Answering questions and summarizing content based on user prompts and potentially local context. 5
- **Content Generation:** Assisting with text generation tasks.<sup>4</sup>
- **File Management (Limited):** While early visions might have suggested extensive file manipulation, current capabilities appear more focused on finding files through improved search rather than direct, complex file operations.<sup>5</sup> For instance, improved Windows Search on Copilot+ PCs allows users to describe what they're looking for in natural language to find files.<sup>9</sup> An upcoming feature, "AI actions in File Explorer," will allow right-click actions like summarizing content or editing images without opening the file. $12$
- **Settings Control (Evolving):** The initial integrated Windows Copilot app had limited ability to directly control Windows OS settings.<sup>5</sup> However, Microsoft announced plans (May 2025) for an "agent in Settings" for Copilot+ PCs, allowing users to describe desired setting changes in natural language, with the AI recommending steps or completing actions with permission. <sup>12</sup> This suggests a move towards more direct OS control, though it's an evolving capability.
- **• "Click to Do" Shortcuts (Preview):** On Copilot+ PCs, this feature offers quick actions like summarizing, copying, or editing on-screen content by clicking Windows Key + mouse button or Windows Key +  $Q^9$ . New actions include creating bulleted lists, and future plans involve leveraging Microsoft 365 Copilot for drafting in Word, scheduling Teams meetings, and sending table data to Excel.<sup>12</sup>

The initial expectation for Windows Copilot to offer comprehensive control over OS settings and intricate local file management has been tempered in its current implementations. While features like the upcoming "Settings agent" and "AI actions in File Explorer" indicate progress, the primary strength of the general Windows Copilot, especially on non-Copilot+ PCs, leans more towards information retrieval, content summarization (often of currently open or easily accessible content), and light task assistance rather than deep system manipulation. The more advanced local data interactions are increasingly tied to the capabilities of Copilot+ PCs. **Underlying Technology & AI Models**

Windows Copilot leverages a combination of on-device and cloud-based AI models.

- **On-Device Models (especially on Copilot+ PCs):** Copilot+ PCs are central to Microsoft's on-device AI strategy. These machines are equipped with NPUs capable of 40+ Trillion Operations Per Second (TOPS). <sup>9</sup> The **Windows Copilot Runtime** provides a suite of APIs and on-device models for AI experiences. <sup>16</sup> This includes **Phi Silica**, a small language model (SLM) developed by Microsoft Research, designed for natural language processing tasks like chat, math, code, and reasoning, running locally on the NPU.<sup>19</sup> Other on-device capabilities powered by the NPU and Windows Copilot Runtime include Text Recognition (OCR) and Studio Effects for cameras.<sup>16</sup>
- **NPUs:** NPUs are specialized processors that accelerate AI computations with greater power efficiency than traditional CPUs or GPUs, enabling more complex AI tasks to run

locally, improving performance, reducing latency, and enhancing privacy.<sup>6</sup> Windows 11 assigns processing tasks to the most appropriate unit (CPU, GPU, or NPU) for optimal performance. 16

● **Balance of Local vs. Cloud Processing:** For general Windows Copilot features available on all compatible PCs, simpler queries or context from open applications might involve some local processing, but more complex queries, web searches, or access to the latest information often rely on cloud-based LLMs (like GPT-4 via Azure OpenAI services). <sup>4</sup> On Copilot+ PCs, features like improved Windows Search and Recall are explicitly designed to run locally using the NPU. $\degree$  Microsoft's strategy is a hybrid one: on-device AI for speed, privacy, and offline capabilities where feasible (especially on Copilot+ PCs), and cloud AI for more demanding tasks or access to broader, up-to-date information. 6

The development of Copilot+ PCs signifies a substantial co-engineering effort between hardware and software. These devices are not merely PCs with an added NPU; they are architected to support a new class of on-device AI experiences. Features like Recall, which continuously processes and indexes screen content, and the enhanced local search capabilities, are fundamentally enabled by the sustained high-performance, low-power AI processing that NPUs provide. <sup>9</sup> This hardware foundation is changing the value proposition of Windows PCs, making sophisticated local AI a key differentiator.

The Windows Copilot Runtime, with its on-device SLMs like Phi Silica and APIs for features like OCR and Studio Effects, is pivotal for this on-device AI push.<sup>19</sup> It provides developers with the tools to build applications that can leverage the NPU's power directly within Windows, leading to more responsive, privacy-centric AI features that don't always require a roundtrip to the cloud. This is a crucial step towards making AI an intrinsic part of the OS and third-party application experience on capable hardware.

#### **Privacy & Data Handling**

Microsoft's approach to privacy and data handling for Windows Copilot distinguishes between personal and commercial use, and increasingly, between standard PCs and Copilot+ PCs with on-device processing.

- **Local Data Access by Windows Copilot:** The general Windows Copilot (not specific features like Recall) can access system information. <sup>5</sup> For tasks like answering questions about how to use the device, it leverages "device context".<sup>8</sup> If a user shares a file with Copilot (e.g., for summarization), it's stored securely for up to 30 days and then deleted; these uploaded files are not used for training generative models. $^{23}$
- **Privacy Controls & User Consent (General Windows Copilot):**
	- **Conversation History:** Saved by default for 18 months; users can view and delete  $it<sup>23</sup>$
	- **Data Usage for Improvement/Personalization:** Microsoft states conversations are used for troubleshooting, bug diagnosis, abuse prevention, and performance improvement.<sup>23</sup> Users can control whether their conversations (for personal

accounts) are used to personalize their experience or train generative AI models.<sup>23</sup> This opt-in/opt-out mechanism is crucial.

- **Organizational Accounts:** Data from users signed in with an organizational Entra ID account is NOT used for training general Copilot models.<sup>23</sup>
- **"Hey, Copilot!" Voice Activation:** This upcoming feature will be opt-in.<sup>12</sup>
- **Settings Agent:** The planned agent for controlling PC settings will require user permission to complete actions. 12
- Data Handling Policies: Microsoft's general Privacy Statement applies.<sup>24</sup> For personal use, users are advised against providing confidential data they wouldn't want Microsoft to use as outlined. 23
- **Local vs. Cloud Processing and Privacy:** For features on Copilot+ PCs like Recall and improved Windows Search, data is explicitly processed and stored locally on the device, not sent to the cloud or shared with Microsoft. $<sup>9</sup>$  This local processing is a key privacy</sup> safeguard for these more data-intensive features. For general Windows Copilot queries that go to the cloud, Microsoft states that for commercial data protection (when signed in with an Entra ID), prompts and responses are processed within the Microsoft 365 service boundary, and are not used to train foundation models.<sup>26</sup> Web grounding via Bing sends anonymized queries. 26

While Windows Copilot aims to utilize local context, its deeper interactions with a user's comprehensive local data (beyond specific tasks like summarizing an open document or answering system-level questions) are still evolving. Features like Recall represent the most significant step in this direction, but their design, heavily influenced by initial privacy concerns, now emphasizes robust user control, opt-in mechanisms, and strong on-device security measures.<sup>9</sup> The general Windows Copilot's access to the broader local file system for proactive assistance or deep contextual understanding, outside of explicit file uploads or features like Recall, is less clearly defined and appears to be an area of ongoing development. **Integration with User Data**

Windows Copilot's integration with user data varies by feature and PC capability:

- **General Windows Copilot:** Can access the content of the active window or explicitly shared files for summarization or contextual  $Q\&A$ .<sup>8</sup> Its access to the broader local file system or application activity for proactive, unprompted assistance is less defined but is a target for future development (e.g., "AI actions in File Explorer" <sup>12</sup>).
- **Copilot+ PC Features:**
	- **Recall:** Deeply integrates with user activity by capturing screen snapshots of files, applications, and websites. <sup>9</sup> This data is indexed locally for search.
	- *O* Improved Windows Search: Leverages local indexing of files and OneDrive content to understand natural language queries about user documents and photos. 9
	- **Click to Do:** Interacts with content visible on the screen, allowing actions on selected text or images.<sup>9</sup>

# **User Experience (UX) & Interface**

Users interact with Windows Copilot through several mechanisms:

- **Sidebar Interface:** A common way to access Copilot, typically docked to the side of the screen. 5
- **Keyboard Shortcut:** Alt + Spacebar brings up a smaller Copilot interface for quick prompts. 5
- **Dedicated Copilot Key:** Featured on new Windows keyboards and Copilot+ PCs, providing one-touch access. 4
- **Voice Interaction:** Users can interact with Copilot using voice commands, with features like "Press to talk" (holding Alt + Spacebar).<sup>8</sup> "Hey, Copilot!" voice activation is planned.<sup>12</sup>
- **Contextual Interactions:** "Click to Do" on Copilot+ PCs allows actions based on on-screen content.<sup>10</sup> Future "AI actions in File Explorer" will offer right-click context menu integration. 12
- **Copilot App:** The April 2025 update integrated Copilot as a standard application, pinnable to the taskbar or Start menu, and downloadable from the Microsoft Store.<sup>5</sup>

# **Availability & Monetization**

Windows Copilot's core functionalities are integrated into Windows 10 (version 19041.0 or later) and Windows 11 as a free feature, part of the operating system. <sup>4</sup> More advanced AI features, particularly those leveraging significant on-device processing like Recall and improved semantic search, are exclusive to Copilot+ PCs, which have specific hardware requirements (NPU, RAM, storage). <sup>9</sup> There is no separate subscription fee for the core Windows Copilot experience or the advanced features on Copilot+ PCs; they are part of the Windows value proposition.

#### **Strengths & Weaknesses**

- **Strengths:**
	- $\circ$  Deep OS integration provides convenient access to AI assistance.<sup>5</sup>
	- Potential for powerful local context understanding, especially with Copilot+ PC features like Recall and improved search.<sup>9</sup>
	- On-device processing on Copilot+ PCs enhances speed, privacy, and offline capabilities for certain AI tasks. 6
	- $\circ$  Free availability as part of the Windows OS.<sup>5</sup>
	- Growing set of features aimed at everyday productivity (e.g., Click to Do, upcoming File Explorer and Notepad AI). 10

#### ● **Weaknesses:**

- $\circ$  Limited OS control and deep file management capabilities in the general version.<sup>5</sup>
- Full potential heavily reliant on new Copilot+ PC hardware for advanced on-device features. 9
- Privacy concerns, particularly with features like Recall, despite mitigations, can

impact user trust. 10

- Effectiveness can be dependent on the quality and organization of local user data for search and contextual features.
- $\circ$  Some user reviews have found the computer control aspects underwhelming.<sup>13</sup>

# **Roadmap & Future Plans**

Microsoft's roadmap for Windows Copilot and OS-level AI, particularly for Copilot+ PCs, indicates a continued push towards deeper integration and more powerful on-device capabilities. Key announcements from Microsoft Build 2024, Ignite 2024, and other communications point to:

- **Enhanced Settings Control:** An "agent in Settings" for Copilot+ PCs to allow natural language control over PC settings (initially for Snapdragon, then AMD/Intel).<sup>12</sup>
- AI in File Explorer: Right-click AI actions for summarizing files or editing images directly from File Explorer.<sup>12</sup>
- AI in Notepad: "Write" and "summarize" functions powered by AI coming to Notepad.<sup>12</sup>
- **Expanded "Click to Do" Actions:** More integrations, including with Microsoft 365 Copilot for drafting in Word, scheduling Teams meetings, and sending data to Excel.<sup>12</sup>
- **Copilot Vision on Windows:** Allowing Copilot to analyze and answer questions about any app window (rolling out). 12
- **Improved Voice Interaction:** "Hey, Copilot!" opt-in voice activation.<sup>12</sup>
- **Continued Development of Windows Copilot Runtime:** Adding more on-device APIs and models to leverage NPUs.<sup>19</sup>
- **Focus on Security and Privacy:** Ongoing efforts to address privacy concerns and build user trust, especially for features like Recall.<sup>10</sup> New Windows security features like Zero Trust DNS and Quick Machine Recovery are also being developed, which, while not directly AI, contribute to a more secure platform for AI.<sup>14</sup>

The overarching strategy for OS-level AI appears to be a hybrid model. On-device processing, particularly on Copilot+ PCs powered by NPUs, is prioritized for tasks requiring speed, low latency, offline access, and enhanced privacy (e.g., Recall, local search, Studio Effects).<sup>6</sup> Simultaneously, cloud-connected AI capabilities remain essential for more complex tasks, accessing vast and up-to-date information (e.g., web-grounded queries), and leveraging larger, more powerful LLMs.<sup>22</sup> This dual approach aims to provide a comprehensive and adaptable AI experience within Windows.

# **User Feedback & Reception**

User feedback for Windows Copilot has been mixed, evolving as the product matures.

- **Positive:** Users generally appreciate the convenience of AI assistance integrated into the OS for tasks like quick information retrieval, summarization, and content generation.<sup>13</sup> The speed and local processing benefits on Copilot+ PCs are anticipated to be well-received.
- **Criticisms:** Early versions of the Windows Copilot app were criticized for

underwhelming computer control capabilities compared to its predecessor, Cortana.<sup>13</sup> Performance issues, such as slowness, have also been noted by some reviewers for cloud-dependent responses.<sup>13</sup> The most significant area of negative feedback has been around privacy concerns, especially for features like Recall, which, despite Microsoft's subsequent changes to make it opt-in and enhance security, faced initial backlash from security experts and privacy advocates.<sup>10</sup>

# **3.2. Microsoft 365 Copilot**

# **Product Overview & Evolution**

Microsoft 365 Copilot was officially announced on March 16, 2023, positioned as an AI-powered productivity tool integrated across Microsoft 365 applications and services.<sup>4</sup> Its primary marketing focus is the enhancement of business productivity by assisting users with tasks like content creation, data analysis, summarization, and communication.<sup>4</sup> Microsoft began testing with 20 initial users, expanding to 600 paying early access customers by May 2023.<sup>4</sup> General availability for Microsoft 365 Enterprise customers (purchasing >300 licenses) started on November 1, 2023. <sup>4</sup> Since its launch, M365 Copilot has seen continuous feature enhancements and deeper integrations across the M365 suite, with regular updates detailed in release notes and highlighted at major Microsoft events like Build and Ignite. $33$

# **Core Features & Functionalities**

Microsoft 365 Copilot is designed to access, understand, and act upon user data within the Microsoft 365 ecosystem. It leverages a user's work context—emails, documents, chats, meetings, calendar—to provide relevant assistance. 33

- **Data Access and Understanding:**
	- *C* **Microsoft Graph Integration:** Copilot uses Microsoft Graph to access user data from OneDrive, SharePoint, Outlook (emails, calendar), Teams (chats, meetings), and other M365 services, respecting existing user permissions.<sup>33</sup>
	- **Contextual Awareness:** It combines this data with the user's current working context (e.g., the document being edited, the ongoing meeting) to provide tailored assistance. 40
- **Application-Specific Capabilities:**
	- **Word:** Drafts text, summarizes documents, rewrites content, answers questions about the document, visualizes content as tables, and can reference cloud files or even entire folders for context. 33
	- **Excel:** Suggests formulas, creates charts, analyzes data to provide insights, helps clean and organize data, and allows graph-grounded chat for insights from broader M365 data. 33
	- **PowerPoint:** Creates presentations from prompts or Word documents (using enterprise templates), adds/edits slides, summarizes decks, adds images, translates presentations, and generates speaker notes.<sup>33</sup>
- **Outlook:** Summarizes email threads, drafts emails (pulling content from other M365 sources), provides coaching on email tone and clarity, and helps schedule meetings. 33
- **Teams:** Summarizes chat conversations (up to 30 days prior) and meetings (using real-time transcripts), answers questions about meetings, captures key points and action items from calls, and facilitates collaborative content creation. <sup>33</sup> Can analyze screen-shared content (coming early 2025). 38
- **OneDrive:** Summarizes files (Word, Excel, PDF, PowerPoint) without opening them, allows users to ask questions about file content, compare files, and generate audio overviews of documents. 33
- **SharePoint:** Copilot in SharePoint allows creating copilots from site content, and authoring engaging web pages leveraging Graph data.<sup>35</sup>
- **OneNote:** Drafts plans, generates ideas, creates lists, organizes information, and can organize multimodal notes (typed, handwritten, voice). $33$
- **Loop:** Facilitates collaborative content creation, summarization, and tracking changes. 33
- *O* **Microsoft 365 Copilot Chat:** A dedicated chat interface (accessible in Teams, M365.com, copilot.microsoft.com) for open-ended prompts, content drafting, and Q&A grounded in work data. <sup>33</sup> Can be grounded in SharePoint/OneDrive folders and third-party data via Graph Connectors. 37

● **General Capabilities:**

- **Summarization:** Across emails, chats, meetings, documents, and presentations.<sup>33</sup>
- **Search and Information Retrieval:** Acts as an intelligent search across the user's M365 data, providing contextually relevant answers.<sup>33</sup>
- **Content Generation:** Drafting documents, presentations, emails, and spreadsheet content. 33
- **Meeting Analysis:** Real-time Q&A, summarization, and action item tracking in Teams meetings. 33
- **Task Automation:** Automating administrative tasks in calls, and through upcoming "Copilot Actions" and agent capabilities.<sup>33</sup>

# **Underlying Technology & AI Models**

The "Copilot System" for Microsoft 365 is an orchestration engine coordinating LLMs, Microsoft Graph, and M365 apps.<sup>40</sup>

- **Large Language Models (LLMs): Microsoft 365 Copilot uses LLMs, including** Generative Pre-trained Transformers like GPT-4, processed via Azure OpenAI services, which are distinct from OpenAI's publicly available services. <sup>4</sup> Azure OpenAI does not cache customer content or Copilot modified prompts for M365 Copilot.<sup>40</sup>
- Microsoft Graph: This is the pivotal component for grounding LLMs in user business data. 33 It provides Copilot with access to the user's emails, chats, documents, calendar, and other M365 data, along with the relationships between these data points and

people. This allows Copilot to retrieve relevant information and understand the user's work context to generate personalized and accurate responses, all while respecting the user's existing permissions. 33

- **Processing Flow:** A user prompt in an M365 app is preprocessed by Copilot, which involves "grounding" it with relevant data accessed via Microsoft Graph from the user's tenant. This grounded prompt is then sent to the LLM (via Azure OpenAI). The LLM generates a response, which Copilot returns to the app and user. 40
- **Model Personalization:** User data within an enterprise context (prompts, responses, data accessed via Graph) is **not** used to train the foundational LLMs used by M365 Copilot. <sup>40</sup> Personalization is achieved at query time by grounding responses in the specific user's organizational data and current working context, facilitated by Microsoft Graph. 40

The effectiveness and safety of Microsoft 365 Copilot are deeply intertwined with an organization's existing data governance practices within the Microsoft 365 ecosystem. Because Copilot relies on Microsoft Graph to access user data according to pre-existing permissions<sup>40</sup>, any deficiencies in information management—such as overly permissive access controls, poorly organized data, or an abundance of redundant, obsolete, or trivial (ROT) data—can directly impact Copilot's performance. If data is not well-managed, Copilot might surface irrelevant information, fail to find critical data, or, more concerningly, inadvertently expose sensitive information to users who technically have access but perhaps shouldn't in a well-governed environment.<sup>46</sup> Microsoft acknowledges this by providing tools and guidance, such as SharePoint Advanced Management for data cleanup and Restricted SharePoint Search for controlling Copilot's data sources <sup>33</sup>, and emphasizing Microsoft Purview for ongoing data security and compliance.<sup>35</sup> This underscores that realizing the full, secure potential of M365 Copilot necessitates a proactive approach to data hygiene and permission management from the customer's side.

#### **Privacy & Data Handling**

Microsoft emphasizes robust data privacy, security, and compliance for Microsoft 365 Copilot, particularly under its "Commercial Data Protection" commitments.

- **Commercial Data Protection:** This refers to a set of controls and commitments ensuring that customer data (prompts, responses, and data accessed via Microso Graph) used by M365 Copilot is protected according to Microsoft 365 commercial terms. <sup>45</sup> Key tenets include:
	- $\circ$  Data remains within the Microsoft 365 service boundary.<sup>40</sup>
	- Customer data is **not** used to train the underlying foundation LLMs.<sup>26</sup>
	- $\circ$  Data is encrypted at rest and in transit.<sup>40</sup>
	- Existing Microsoft 365 security, compliance, identity, and privacy policies (including GDPR and EU Data Boundary commitments) apply to M365 Copilot. 40
- **Data Residency:** M365 Copilot upholds data residency commitments. The content of interactions is stored based on the user's Preferred Data Location (PDL) or the tenant's

Primary Provisioned Geography if PDL is not set.<sup>40</sup> Microsoft 365 Copilot was added as a covered workload for data residency commitments on March 1, 2024.<sup>40</sup>

- **Tenant Isolation:** Data is isolated within the customer's Microsoft 365 tenant, and Copilot respects these boundaries. 40
- **Data Collection, Storage, Processing:**
	- User prompts and Copilot responses (including citations) are stored within the Microsoft 365 service boundary.<sup>40</sup> Admins can use Content Search or Microsoft Purview to view, manage, and set retention policies for this data. <sup>40</sup> For Teams chats with Copilot, Teams Export APIs can also be used. 40
	- Processing occurs via Azure OpenAI services, not OpenAI's public services.<sup>40</sup>
	- M365 Copilot does not appear to leverage on-device processing capabilities of Copilot+ PCs for its core functionalities; it is primarily a cloud-based service interacting with cloud-hosted M365 data and Azure AI. 40
- **User Consent:** Deployment and use of M365 Copilot are typically governed by organizational policies. Admins control plugin access, and users choose which plugins to activate.<sup>40</sup> For specific features like Teams meeting recording/transcription, explicit participant consent can be required via admin policies. 35
- **Responsible AI Principles:** Microsoft states M365 Copilot is developed in line with its Responsible AI principles, including safeguards against harmful content and prompt injection attacks.<sup>1</sup> The Customer Copyright Commitment offers protection for intellectual property concerns. 45

The "Commercial Data Protection" framework is a cornerstone of Microsoft's strategy for enterprise AI. In a landscape where businesses are increasingly wary of how their proprietary information might be ingested and utilized by third-party AI models, Microsoft's explicit commitment that M365 Copilot interactions and accessed business data will not be used to train the foundational LLMs is a significant assurance.<sup>40</sup> This policy, combined with tenant data isolation and adherence to existing M365 compliance and security boundaries <sup>40</sup>, directly addresses key enterprise concerns. It allows organizations to leverage powerful generative AI capabilities while maintaining control over their data and mitigating risks of data leakage into public models or use by the AI vendor for general model improvement. This stance is crucial for building the trust necessary for widespread enterprise adoption of AI tools that interact deeply with sensitive business information.

#### **Integration with User Data**

Microsoft 365 Copilot achieves deep integration with user data primarily through Microsoft Graph.<sup>33</sup> Microsoft Graph serves as the API gateway to data and intelligence in the Microsoft 365 ecosystem. It allows Copilot to:

- Access a user's emails, calendar events, and contacts from Outlook.
- Retrieve and understand documents from OneDrive and SharePoint.
- Analyze chat history and meeting transcripts from Teams.
- Understand the user's organizational context, such as their role, team, and reporting

structure. This deep integration enables Copilot to provide highly contextual and personalized assistance, grounding its responses in the user's actual work content and activities, all while respecting the existing permissions and security boundaries defined within the Microsoft 365 tenant. $40<sup>10</sup>$

The centrality of Microsoft Graph to M365 Copilot's functionality cannot be overstated. It acts as the connective tissue, transforming the LLM from a general-purpose text generator into a true work assistant that understands the user's specific context.<sup>33</sup> By providing a structured, permission-aware pathway to the vast and varied data within an enterprise's M365 tenant (emails, files, chats, calendars, etc.), Microsoft Graph enables Copilot to deliver relevant summaries, draft pertinent documents, and answer questions based on the user's actual work. This rich, contextual grounding is a key differentiator for M365 Copilot compared to AI assistants that lack such native and comprehensive access to an organization's internal data fabric. Furthermore, the extensibility of Graph through connectors, which can be leveraged by Copilot Studio, allows this contextual understanding to potentially span beyond M365 data to other enterprise systems. 35

#### **User Experience (UX) & Interface**

Users interact with Microsoft 365 Copilot through interfaces embedded within the M365 applications they already use, as well as through dedicated chat experiences.<sup>33</sup>

- **In-App Integration:** Copilot features are typically accessible via ribbons, side panes, or contextual menus within Word, Excel, PowerPoint, Outlook, and Teams. This allows users to invoke AI assistance directly in their workflow without switching applications. For example, a Copilot icon might appear in a spreadsheet for quick AI assistance.<sup>35</sup>
- **Microsoft 365 Copilot Chat:** This provides a dedicated conversational interface, accessible via Microsoft Teams, Microsoft365.com, and copilot.microsoft.com, where users can engage in open-ended dialogue with Copilot, ask questions, draft content, and get insights based on their work data.<sup>33</sup>
- **Prompting:** Users interact by typing natural language prompts. Copilot may also offer suggested prompts based on context or previous interactions.<sup>35</sup>
- **Copilot Pages:** A feature allowing insightful Copilot responses to be turned into editable, shareable pages for team collaboration. 36

#### **Open Source Aspects**

While Microsoft 365 Copilot itself is a proprietary commercial product, Microsoft provides SDKs and tools that have open-source components or are hosted on open platforms like GitHub, enabling developers to extend and customize Copilot experiences.

- **Microsoft 365 Agents SDK:** This SDK allows developers to create custom agents that can be used in M365 Copilot, Teams, and other applications. Starter samples in C#, JavaScript, and Python are available on GitHub. <sup>55</sup> The documentation site for the SDK is also open source. 58
- **Copilot Studio Samples:** Microsoft provides various samples for Copilot Studio on GitHub, which can be used to build custom copilots and extensions.<sup>59</sup>

# **Availability & Monetization**

Microsoft 365 Copilot is available as an add-on license for qualifying Microsoft 365 commercial plans, such as Microsoft 365 E3, E5, Business Standard, and Business Premium.<sup>49</sup>

- **Pricing:** The standard price is \$30 per user per month, typically with an annual commitment.<sup>49</sup> Monthly payment options may be available at a slight premium.<sup>49</sup>
- **Prerequisites:** Users must have an eligible base M365 license, Microsoft Entra ID accounts, and often OneDrive accounts for certain features. Microsoft 365 Apps must be deployed. 56
- **Specialized SKUs:** Microsoft also offers specialized versions like Copilot for Sales, Copilot for Service, and Copilot for Finance, which provide capabilities tailored to those roles and may integrate with CRM/ERP systems. These may have different licensing or bundling options. 49

#### **Strengths & Weaknesses**

- **Strengths:**
	- Deep integration with widely used Microsoft 365 productivity applications, providing AI assistance directly within user workflows. $^{28}$
	- Powerful contextual understanding and data retrieval capabilities through Microsoft Graph, grounding responses in user-specific enterprise data.<sup>33</sup>
	- Strong enterprise security, privacy, and compliance posture, including "Commercial Data Protection" and adherence to tenant boundaries and data residency policies. 28
	- Extensive developer ecosystem for customization and extension via Copilot Studio and the M365 Agents SDK. 53
	- $\degree$  Reported productivity gains and time savings for users and organizations.<sup>57</sup>
- **Weaknesses:**
	- Cost can be a significant barrier to adoption for some organizations, especially for broad deployment. 49
	- $\circ$  Effectiveness is highly dependent on the quality of an organization's data governance and information management practices within Microsoft 365.<sup>33</sup>
	- Potential for generating plausible but incorrect or incomplete information if not prompted carefully or if underlying data is flawed, requiring user vigilance and review. 28
	- Learning curve for users to master effective prompting and leverage advanced features. 28
	- Primarily cloud-based, relying on Azure AI, with limited on-device processing for core M365 Copilot features. 40

#### **Roadmap & Future Plans**

Microsoft is continuously evolving Microsoft 365 Copilot with new features and capabilities,

often announced at events like Build and Ignite.

- **Team Copilot:** An expansion of Copilot to function as a collaborative team member in Teams, Loop, Planner, assisting with meeting facilitation, group collaboration, and project management. Preview expected later in 2024/early 2025.<sup>7</sup>
- **Custom Copilots in SharePoint:** Empowering users to create copilots grounded in the content of specific SharePoint sites. Preview expected later in 2024/early 2025.<sup>39</sup>
- **Copilot Actions:** Customizable prompt templates that can be automated or triggered by events to delegate repetitive tasks to Copilot.<sup>38</sup>
- **•** Deeper Microsoft Graph Integration:
	- People connectors for Microsoft 365 Copilot will integrate and enrich people data from various sources into M365, enhancing Copilot Chat, profile cards, and people search (Preview May 2025, General Availability August 2025). 52
	- Grounding M365 Copilot Chat prompts in third-party data from Microsoft Graph Connectors (Expected May-June 2025). 37
	- Grounding M365 Copilot prompts in specific SharePoint/OneDrive folders and sites (Expected May-June 2025). 37
- **Continued Application Feature Enhancements:** Ongoing updates across Word, Excel, PowerPoint, Outlook, Teams, and OneNote, including analyzing screen-shared content in Teams (early 2025), summarizing shared files in Teams chat (early 2025), and new data interaction capabilities. 35
- **Copilot Studio Evolution:** Further development of autonomous agent capabilities, deeper Azure AI integration (including Azure AI Foundry), new connectors, and enhanced governance features are planned for Copilot Studio, which extends M365 Copilot. 38

# **User Feedback & Reception**

User and enterprise reception for Microsoft 365 Copilot has been largely positive, focusing on productivity benefits, though cost and the need for good data hygiene are common discussion points.

- **Positive Feedback:** Many users and organizations report significant productivity gains, time savings (e.g., 11 minutes per day on average, up to 30 minutes for efficient users; 31% less time reading emails at one company), and assistance with routine and creative tasks.<sup>28</sup> Features like summarization, drafting, and data analysis are frequently praised.<sup>28</sup> Businesses like Aberdeen City Council project substantial ROI (241%) from time savings and improved productivity. 64
- **Criticisms and Challenges:**
	- The cost of \$30/user/month is a significant consideration for many organizations. 62
	- Occasional inaccuracies or "hallucinations" in responses, requiring users to verify information. 28
	- The need for careful and specific prompting to get the best results; there's a

learning curve involved. 28

- Concerns about intellectual property if not used carefully, though Microsoft offers an IP indemnification commitment.<sup>28</sup>
- The quality of Copilot's output can be diminished if an organization's underlying M365 data is poorly managed or permissions are not correctly configured.<sup>46</sup>

# **3.3. Microsoft Recall (Status as of May 2025)**

# **Product Overview & Evolution**

Microsoft Recall was announced as a flagship AI feature for the new category of Copilot+ PCs, designed to create a searchable, visual timeline of a user's activity on their PC, effectively acting like a "photographic memory" for their computer usage.<sup>9</sup> Its unveiling in May 2024 was met with immediate and significant privacy and security concerns from experts and the public, who dubbed it a potential "privacy nightmare" due to its continuous screen capturing. 10

In response to this backlash, Microsoft delayed the broad rollout of Recall and announced significant changes to its design and security architecture.<sup>9</sup> These changes included making Recall an opt-in experience rather than on-by-default, strengthening encryption, requiring biometric authentication via Windows Hello Enhanced Sign-in Security (ESS), and ensuring all data processing and storage remained strictly local to the device.<sup>9</sup>

A preview of the redesigned Recall was made available to Windows Insiders on Copilot+ PCs in November 2024.<sup>10</sup> The broader rollout to all Copilot + PC users commenced with the April 2025 and May 2025 Windows non-security preview updates and Patch Tuesday updates, respectively. 10

# **Core Features & Functionalities**

- **Functionality:** Recall continuously captures snapshots (screenshots) of the user's screen activity every few seconds, encompassing applications, websites, documents, images, and communications.<sup>9</sup> This creates a chronological, visual timeline that users can scroll through to find past activities.<sup>9</sup> Users can also search this timeline using natural language, describing content they remember seeing, and Recall will find relevant snapshots. 9
- **Data Capture Methods:** The system automatically takes screenshots in the background when enabled.<sup>10</sup> It then creates a semantic index of the content (text and images) within these snapshots to facilitate searching  $\int^9$  (referencing Recall architecture update)].
- **On-Device Processing & NPU Utilization:**
	- All data captured by Recall (snapshots and the semantic index) is stored and processed exclusively locally on the Copilot+  $PC$ .<sup>9</sup> No data is sent to Microsoft's cloud servers or shared with Microsoft or third parties.<sup>9</sup>
	- $\circ$  Recall is a demanding feature that requires a Copilot + PC equipped with a Neural

Processing Unit (NPU) capable of at least 40 TOPS, along with 16 GB RAM and sufficient SSD storage (at least 256 GB, with 50 GB free for Recall).<sup>9</sup>

- The NPU is critical for the continuous, on-device AI processing involved in capturing, analyzing, indexing, and encrypting screen content efficiently without significantly impacting overall system performance or battery life.<sup>16</sup> Recall utilizes the NPU and the Microsoft Classification Engine (MCE) for its on-device operations. 18
- The security architecture involves "just-in-time" decryption of snapshots, protected by Windows Hello Enhanced Sign-in Security (ESS), with operations occurring within secure Virtualization-based Security (VBS) Enclaves [<sup>9</sup> (referencing Recall architecture update)].

# **Privacy & Data Handling (CRITICAL)**

Given its nature, privacy and data handling are paramount for Recall. Microsoft has implemented multiple layers of protection and user control in response to initial concerns:

- **Privacy Implications:** The core function of continuously recording screen activity inherently raises privacy risks, including the potential capture of sensitive information (passwords, financial data, private messages) and images of other individuals who might be visible on screen or in communications.<sup>10</sup>
- **User Controls & Consent:**
	- **Opt-in Experience:** Recall is strictly opt-in. Users must explicitly choose to enable the feature during the Copilot+ PC setup process or later through settings. If not enabled, no snapshots are taken or saved.<sup>9</sup>
	- **Authentication for Access:** Launching Recall and accessing the timeline or snapshots requires user authentication via Windows Hello Enhanced Sign-in Security (ESS), with at least one biometric option (facial recognition or fingerprint) enabled. 9
	- **Eiltering and Exclusion:** Users can configure Recall to exclude specific applications or websites (when browsed in InPrivate mode in supported browsers like Edge) from being captured in snapshots  $\int^9$  (referencing Recall architecture update)].
	- **Snapshot Storage Management:** Users have control over how much disk space Recall can use for storing snapshots. Saving automatically pauses if free disk space falls below 25 GB.<sup>18</sup> Users can delete individual snapshots, ranges of snapshots (e.g., last hour, last day), all snapshots related to a specific app or website, or the entire Recall history at any time  $\int^9$  (referencing Recall architecture update)].
	- **Pausing Snapshots:** Users can pause snapshot saving at any time, for example, via a system tray icon [ 9 (referencing Recall architecture update)].
	- **Sensitive Content Filtering:** A feature is enabled by default to detect and attempt to avoid saving snapshots containing potentially sensitive information like passwords, financial account numbers, or national ID numbers. This uses

on-device Microsoft Classification Engine (MCE) technology, similar to that in Microsoft Purview [<sup>9</sup> (referencing Recall architecture update)].

- **DRM-Protected Content:** Recall is designed not to save snapshots of content protected by Digital Rights Management (DRM). 18
- **Data Handling & Security:**
	- **Local Storage and Processing:** All snapshots and the associated semantic index (vector database) are stored and processed locally on the user's device hard drive. 9
	- **Encryption:** Snapshots and the index are encrypted using BitLocker Drive Encryption (or Windows Device Encryption on Home editions), which must be enabled. <sup>18</sup> Further, data is protected with "just-in-time" decryption performed within a secure VBS Enclave and keys are cryptographically bound to the user's identity and sealed by the device's Trusted Platform Module (TPM) 2.0  $\int^9$ (referencing Recall architecture update)]. This means data is only decrypted when actively requested by an authenticated user.
	- **O No Cloud Sharing or Microsoft Access:** Microsoft has repeatedly stated that Recall data is not sent to Microsoft's cloud, is not accessible by Microsoft, and is not used to train any AI models.<sup>9</sup> Data is also not shared between different user accounts on the same device. 25
	- **Managed Devices:** For enterprise environments, Recall is not available by default on managed devices. Administrators can use policies (e.g., Group Policy or MDM like Intune) to control whether Recall can be enabled by users in their organization.<sup>18</sup>
- **Responsible AI Considerations: Microsoft's significant revisions to Recall's** architecture and user control mechanisms following public feedback demonstrate an application of its Responsible AI principles, particularly concerning privacy, security, transparency, and user control [ 9 (referencing RAI document and Recall architecture update)]. The UK's Information Commissioner's Office (ICO) engaged with Microsoft regarding Recall, emphasizing the need for user transparency and ensuring data is used only for its original collected purpose.<sup>25</sup>

Recall represents one of Microsoft's most ambitious moves towards creating an "AI second brain" for PC users, offering the powerful ability to find virtually anything previously seen on their screen. <sup>9</sup> However, this capability comes with inherent privacy implications due to its continuous screen capture mechanism. <sup>25</sup> The success and acceptance of Recall will largely depend on the perceived and actual robustness of the multi-layered privacy and security measures Microsoft has implemented. The shift to an opt-in model, mandatory biometric authentication, on-device encrypted storage processed within secure enclaves, and granular user controls are all critical steps to build user trust.<sup>9</sup> If users are confident that their data remains private, secure, and under their control, Recall could become a transformative productivity tool. Conversely, any security lapse or perceived overreach could significantly damage trust in Microsoft's broader AI ambitions.

The NPU is the linchpin technology that makes Recall feasible in its current privacy-focused, on-device form. <sup>18</sup> The sheer volume of data generated by continuous screen capture, coupled with the AI processing required for analysis, indexing, and encryption, would place an enormous burden on traditional CPU/GPU resources, likely leading to unacceptable performance degradation or forcing a reliance on cloud processing. <sup>16</sup> Cloud processing for such sensitive, comprehensive data would have amplified privacy concerns exponentially. The NPU's ability to handle these AI-specific workloads efficiently and locally is therefore fundamental to Recall's design, enabling both its powerful functionality and its "data stays local" privacy promise.<sup>9</sup>

# **Availability & Monetization**

Microsoft Recall is an exclusive feature of **Copilot+ PCs**.<sup>9</sup> These PCs must meet specific hardware requirements, including a capable NPU (40+ TOPS), minimum 16 GB RAM, and 256 GB SSD with at least 50 GB free space for Recall to be enabled.<sup>17</sup> Recall is included as a feature of the Windows 11 operating system on these qualifying devices and is not monetized as a separate subscription or add-on. Its availability is tied to the purchase of a Copilot+ PC.

# **3.4. Edge Copilot & Browser AI Features**

# **Product Overview & Evolution**

Copilot in Microsoft Edge, initially launched as Bing Chat in Edge in February 2023, was one of Microsoft's earliest integrations of generative AI into a mainstream product.<sup>4</sup> It has since evolved from primarily a chat-based AI search assistant into a more deeply integrated browser companion. Its capabilities have expanded to include contextual page summarization, content generation (including images), and direct interaction with web content. 70 As of May 2025, the broader Microsoft Copilot service (which Edge Copilot is part of) saw updates like the worldwide availability of Copilot Pages (for organizing AI-assisted work), the introduction of Deep Research for Copilot Pro users (for comprehensive web research), new Hispanic voice options (Alder and Elm), and an increased file upload limit to 50MB.<sup>74</sup> Specifically for Edge, a Microsoft 365 Copilot Chat Summarization feature in the context menu is planned for rollout in June 2025 for Edge for Business users.<sup>75</sup>

#### **Core Features & Functionalities**

Edge Copilot and other AI features in the browser leverage browsing activity and web content to provide assistance:

- **Contextual Summarization & Search:** Copilot in Edge can summarize the content of the current web page, article, or even YouTube videos. It can answer user questions based on the information present on the open page.<sup>70</sup> Users can also highlight specific text on a page and use the "Ask Copilot" feature to get targeted assistance or information about that selection. 70
- **Content Generation:** Includes Image Creator, powered by DALL-E models, allowing users to generate images from text prompts directly within the browser. <sup>4</sup> Copilot can

also assist in drafting text.

- **Copilot Actions (Coming for Copilot Pro subscribers):** This feature aims to allow users to perform web-based tasks, such as making reservations or travel bookings, using conversational prompts. 70
- Copilot Daily: Provides personalized information like news, weather, and reminders.<sup>70</sup>
- **@Copilot in Address Bar:** Typing @copilot in the Edge address bar provides quick access to the AI assistant. 70
- **AI-Powered Tab Organization:** Edge can automatically create tab groups based on tab similarity, helping users manage multiple open tabs.<sup>71</sup>
- AI Theme Generator: Users can generate custom browser themes using text prompts.<sup>71</sup>
- **Read Aloud:** An AI-powered text-to-speech feature that reads web page content aloud with natural-sounding voices.<sup>71</sup>
- **Text Prediction:** Offers AI-powered text predictions as users type in web forms or text fields. $71$
- **Editor Integration:** Microsoft Editor is built into Edge, providing AI-powered spelling, grammar, and synonym suggestions across the web. 71
- **Scareware Blocker:** Uses machine learning to detect and block full-screen pop-ups associated with scareware attacks. $71$

# **Underlying Technology & AI Models**

Copilot in Edge is built upon Microsoft's broader AI infrastructure, primarily utilizing Large Language Models (LLMs).

- **LLMs:** It leverages OpenAI's models, such as GPT-4 for conversational AI and DALL-E 3 for image generation.<sup>4</sup> Microsoft's own Prometheus model, which builds upon and enhances GPT-4, is also likely a core component. 4
- **Local vs. Cloud Processing:** The core AI functionalities of Edge Copilot, such as natural language understanding, summarization of web pages, content generation, and complex query responses, are predominantly **cloud-based**. <sup>22</sup> These tasks require the significant computational power and access to extensive datasets that cloud platforms like Azure AI provide.<sup>22</sup> While some lighter AI-driven browser features like the scareware blocker or potentially aspects of text prediction might involve local processing or on-device models (especially on Copilot + PCs with NPUs)<sup>71</sup>, the heavy lifting for conversational AI and deep content analysis relies on cloud infrastructure. Microsoft's general guidance highlights that LLMs are resource-intensive and typically cloud-hosted, whereas smaller models like Phi are more suited for local execution. $^{22}$ Given Edge Copilot's deep web integration and complex language processing needs, substantial cloud reliance is inherent.

# **Privacy & Data Handling**

The use of browsing data by Edge Copilot necessitates clear privacy policies and user controls.

- **Browsing Data Access:** Copilot in Edge can access the content of the active web page to provide summaries, answer contextual questions, and support features like "Ask Copilot" on highlighted text. 70
- **User Consent & Controls:**
	- Users have explicit control over whether Copilot in Edge can access page content. This is managed via a toggle in Edge settings: Settings > Sidebar > Copilot > Allow Microsoft to access page content.<sup>76</sup>
	- For enterprise environments, administrators can use Group Policy settings such as EdgeEntraCopilotPageContext (to control page content access for Entra ID users) and CopilotPageContext (to control page content access for personal MSA Bing accounts in an Edge work profile).<sup>76</sup> The HubsSidebarEnabled policy can disable the Edge sidebar, including Copilot, entirely.<sup>76</sup>
- **Data Handling:**
	- Microsoft's general Privacy Statement applies to data collected through Edge and Copilot. 24
	- **Example 7 For Microsoft 365 Copilot users** (i.e., commercial users with an Entra ID signed into Edge), when Copilot accesses work-related content or is used in a work context, prompts and responses generally remain within the Microsoft 365 service boundary, adhering to commercial data protection principles. Web search queries made by Copilot via Bing are sent with user and tenant identifiers removed, are not shared with advertisers, and are not used to train foundation LLMs.<sup>26</sup>
	- $\circ$  For **personal Copilot use in Edge** (e.g., with a personal Microsoft Account), conversation history is saved by default but can be managed (viewed, deleted) by the user. Data from these interactions may be used for personalization and to improve Copilot models, subject to user opt-out choices available in privacy settings.<sup>23</sup>
- **Responsible AI:** Microsoft's overarching Responsible AI principles are intended to govern the development and deployment of Edge Copilot features.<sup>1</sup> This includes efforts to mitigate harmful content and ensure transparency.

Edge Copilot serves as a significant touchpoint for Microsoft to understand how users interact with AI in a web context. The data from these interactions (anonymized or aggregated where specified by privacy policies and user consent) provides valuable feedback for refining Bing's search algorithms, the underlying Prometheus model, and the overall effectiveness of web-grounded AI responses across the entire Copilot ecosystem.<sup>26</sup> This continuous loop of interaction and refinement is crucial for Microsoft's competitive stance in AI-powered web services.

# **User Experience (UX) & Interface**

Copilot in Edge is designed for seamless integration into the browsing workflow:

● **Sidebar Integration:** The primary interface is a sidebar, typically on the right, which can be opened by clicking the Copilot icon.<sup>70</sup> This allows users to interact with Copilot without leaving their current web page.

- **Address Bar Access:** Users can type @copilot into the Edge address bar for quick access. 70
- **Contextual Menus:** The "Ask Copilot" feature appears when text is highlighted on a page, allowing for context-specific queries.<sup>70</sup>
- **Interaction Methods:** Supports both typed text prompts and voice input.<sup>70</sup>

# **Availability & Monetization**

The core AI features of Copilot in Microsoft Edge, including page summarization, contextual Q&A, and image generation, are available for free as part of the standard Edge browser.13 This strategy aims to enhance the value proposition of Edge and drive its adoption. However, Microsoft is introducing a tiered approach for more advanced capabilities. Certain upcoming features, such as Copilot Actions (which will allow conversational prompts to complete web tasks like reservations), are slated to be available exclusively for Copilot Pro subscribers.70 Copilot Pro is a paid subscription (\$20 per month) that also offers benefits like priority access to newer AI models (e.g., GPT-4 Turbo) and higher usage limits for features like image generation across the broader Copilot ecosystem.13

This dual monetization strategy—offering robust core AI assistance for free to attract users to Edge, while reserving more advanced automation and power-user features for a premium subscription—allows Microsoft to both leverage AI as a platform differentiator and generate direct revenue from users seeking enhanced AI capabilities.

# **Strengths & Weaknesses**

# ● **Strengths:**

- Seamless integration directly within the Edge browser, providing AI assistance without context switching.<sup>13</sup>
- Strong contextual understanding of web page content for relevant summaries and  $OSA<sup>70</sup>$
- Access to up-to-date information through Bing integration for web-grounded responses. 13
- Free availability of powerful AI models (like GPT-4 and DALL-E 3) for core features enhances Edge's value proposition. 13
- Growing suite of AI-powered browser utilities (tab organization, theme generator, read aloud). 71

# ● **Weaknesses:**

- Heavy reliance on cloud processing for most significant AI tasks, which can introduce latency and requires internet connectivity.<sup>13</sup>
- Privacy considerations related to browser data access, although user controls and distinct policies for personal/commercial use are in place.<sup>23</sup>
- Some of the most advanced upcoming features (e.g., Copilot Actions) are gated behind the Copilot Pro subscription. 70
- Like all LLM-based tools, responses can occasionally be inaccurate or require careful prompting.

#### **Roadmap & Future Plans**

Microsoft continues to invest in enhancing AI capabilities within the Edge browser.

- **Copilot Actions:** The rollout of Copilot Actions for Copilot Pro subscribers, enabling automation of web tasks through conversational prompts, is a key future development.<sup>70</sup>
- **Microsoft 365 Copilot Chat Summarization in Edge for Business: A context menu** item for M365 Copilot users in Edge for Business to quickly summarize and ask questions about the open page is planned for rollout starting June 2025.<sup>75</sup>
- **Deep Research:** This feature, currently in English for Pro users, uses advanced reasoning models for comprehensive web research and is expected to support additional languages. 74
- **Ongoing Enhancements:** Continuous improvements to existing features, model accuracy, and user experience are expected, as indicated by regular release notes for the broader Copilot service.<sup>37</sup> The Microsoft 365 Roadmap also lists an item for M365 Copilot to provide an overview of recent comments and changes in Word, Excel, and PowerPoint files via the Copilot chat pane, which could potentially be accessed through Edge if the user is in the web versions of those apps (Rollout Start June 2025).<sup>79</sup>

# **3.5. Microso Copilot Studio**

# **Product Overview & Evolution**

Microsoft Copilot Studio is a comprehensive low-code platform designed for creating, customizing, and managing AI-powered copilots (often referred to as AI agents).<sup>53</sup> It represents an evolution from Microsoft Power Virtual Agents, significantly rebranded and expanded in capabilities to align with Microsoft's broader Copilot strategy and the increasing demand for tailored AI solutions. Its core purpose is to empower both citizen developers and professional developers to build sophisticated conversational AI experiences that can integrate with enterprise data and extend the functionality of Microsoft 365 Copilot.<sup>81</sup> Key evolutionary trends since early 2023 include:

- **Deeper Integration with Microsoft 365 Copilot:** Enabling the creation of custom agents and plugins that seamlessly operate within and enhance the standard M365 Copilot experience. 35
- **Enhanced Generative AI Capabilities:** Leveraging advancements in LLMs and generative AI to allow for more natural conversation design, dynamic content generation, and sophisticated reasoning within custom copilots. 53
- **Integration with Azure AI Services:** Tighter connections with Azure AI Foundry, Azure OpenAI Service, and Azure AI Search allow custom copilots to utilize powerful backend AI infrastructure and models.<sup>3</sup>
- **Advanced Agentic Features:** Introduction of capabilities like autonomous agents that can act on events without direct prompting, and "computer use" for UI automation, moving beyond simple Q&A bots. 38
- **Expanded Data Connectivity:** Growing library of connectors and improved

mechanisms for grounding copilots in diverse enterprise data sources.<sup>35</sup>

The 2025 Release Wave 1 (covering April to September 2025) for Copilot Studio highlights continued focus on areas such as using Azure OpenAI on customer data, leveraging Azure AI Search as a knowledge source, providing prebuilt agents as starting points, further extending M365 Copilot, and enhancing configuration, authoring, and governance capabilities.  $67$

#### **Core Features & Functionalities**

#### ● **Creating Custom AI Assistants:**

- Provides a graphical, low-code interface for designing conversational flows, defining topics, and managing agent behavior. $80$
- Supports natural language understanding for creating agents by describing desired functionality. 80
- Agents can be tailored for specific tasks, roles (e.g., HR support, IT helpdesk), or industries.

#### ● **Integration with Enterprise Data:**

- **Example 2 Microsoft Graph Connectors:** Enables custom copilots to be grounded in enterprise data residing in Microsoft Graph, including SharePoint, OneDrive, and data from third-party systems connected via Graph connectors. <sup>35</sup> This allows agents to provide contextually relevant responses based on organizational knowledge.
- **Power Platform Connectors:** Leverages the extensive library of Power Platform connectors to integrate with hundreds of other data sources and services, both Microsoft and third-party. $53$
- **Custom APIs and Plugins:** Supports calling external APIs and building custom plugins for bespoke integrations. 80
- **Knowledge Sources:** Custom copilots can use public websites, SharePoint sites, uploaded documents, and Azure AI Search indexes as knowledge bases to answer questions and provide information. <sup>55</sup> Teams chats are also planned as a knowledge source. 67
- New connectors for Asana, Miro, Trello, Zendesk, and Smartsheet were added in April 2025, further expanding data integration options. 53
- **Extending Microsoft 365 Copilot:**
	- A key use case is building custom agents, plugins, or "Copilot extensions" that enhance the standard Microsoft 365 Copilot with company-specific knowledge, business logic, and actions.<sup>7</sup> These extensions can be published and made available within M365 Copilot Chat and other M365 applications. 39
- **Agentic and Automation Capabilities:**
	- Autonomous Agents: Copilot Studio supports the creation of agents that can operate autonomously in the background, responding to events (e.g., new email, file upload) and executing tasks without continuous human prompting. $38$ Generative orchestration and analytics for autonomous agents are being

enhanced. 53

- **Computer Use (UI Automation):** A research preview feature introduced in April 2025 allows agents to interact directly with the graphical user interfaces (GUIs) of websites and desktop applications (e.g., clicking buttons, entering data into fields) even if no APIs are available. This is a significant step towards broader automation capabilities. 53
- **Agent Flows (Automation):** Enables the automation of multi-stage business processes, with distinct steps and decision-makers. Advanced approvals within agent flows are in public preview.<sup>53</sup>
- **Actions:** Agents can perform actions by calling Power Automate flows, custom APIs, or other connected services.<sup>81</sup>
- **Multi-modal Capabilities:**
	- **Voice Interaction:** Supports integration with Interactive Voice Response (IVR) systems, enabling voice-enabled agents with features like speech recognition, interruption handling, and re-prompts. 60
	- **Image Handling:** Allows users to upload images to copilots, which can then be analyzed (e.g., using GPT-40) for Q&A or other tasks.<sup>38</sup>
- **Component Reusability:** Features like "Component Collection" allow makers to import, manage, and export core agent components (topics, knowledge, actions, entities) for reuse across different agents and environments.<sup>55</sup>

# **Underlying Technology & AI Models**

Copilot Studio is built on Microsoft's Power Platform and deeply integrates with Azure AI services.

- **Azure AI Services:** It leverages various Azure AI capabilities, including:
	- **Azure OpenAI Service:** Provides access to powerful LLMs like GPT-4 and GPT-4o (e.g., for image analysis features). 38
	- **Azure AI Search (formerly Cognitive Search):** Can be used as a knowledge source for custom copilots, enabling them to search and retrieve information from indexed enterprise data. 67
	- **Azure AI Foundry:** Integration with Azure AI Foundry allows access to a broader range of prebuilt or custom AI models (including Microsoft's Phi-family, DeepSeek R1, and other third-party models) and advanced tuning capabilities. $3$
- **Language Models:** While specific model versions are continuously updated, the platform is designed to work with state-of-the-art LLMs for natural language understanding, generation, and reasoning. 81
- **Orchestration:** Copilot Studio itself acts as an orchestration layer, managing conversational flow, context, knowledge retrieval, action execution, and integration with backend systems. 81
- **Local vs. Cloud Processing:** Copilots created with Copilot Studio are predominantly **cloud-processed**. The platform itself is a web-based application, and the agents it builds leverage Azure's cloud infrastructure for AI model inference, data connections,

and workflow automation.<sup>22</sup> The "computer use" feature for UI automation, for example, runs on Microsoft-hosted infrastructure.<sup>83</sup> While custom copilots might interact with on-device applications or data if designed to do so (e.g., via a local gateway for Power Automate), the core intelligence and processing of the Copilot Studio platform and the agents it generates reside in the cloud. There is no significant indication of direct NPU-based on-device processing for the agents *created by* Copilot Studio itself, although these agents could theoretically trigger actions or interact with other services that do have on-device components.

#### **Privacy, Data Handling, and Security**

Microsoft provides several mechanisms to address privacy, data handling, and security for copilots built with Copilot Studio:

- **Data from Connected Sources (e.g., Microsoft Graph): When Copilot Studio agents** connect to data sources like Microsoft Graph, SharePoint, or other enterprise systems, they are designed to respect the security and permission models of those sources.<sup>47</sup> The agent only accesses data that the authenticated user (or the agent's service identity) has permissions for.
- **User Interactions:** Data from user interactions with custom-built copilots (prompts, responses) is handled according to the configurations set by the organization. Admins have controls over data logging and retention.
- **Admin Controls and Governance:**
	- Admins can manage agent deployment, sharing, and access to data sources and connectors. 35
	- The Power Platform admin center provides tools for managing environments, licenses, and security settings for Copilot Studio.<sup>85</sup>
	- Security-related views and statuses for agents are being added to Copilot Studio. 67

#### ● **Encryption and Security:**

- Copilot Studio now supports **Customer Managed Keys (CMKs)**, allowing organizations to use their own encryption keys (hosted in Azure Key Vault) to encrypt their agent data at rest. This provides greater control over data protection, including the ability to rotate and revoke keys. 53
- Standard Microsoft cloud security measures apply to the platform and data processed within it [<sup>89</sup> (general Security Copilot docs, implies broader Microsoft security stance)].
- **Responsible AI Principles and User Consent:**
	- Microsoft provides guidelines for developing AI responsibly, and these are applicable to copilots built with Copilot Studio. <sup>87</sup> This includes considerations for fairness, reliability, safety, privacy, inclusiveness, transparency, and accountability.
	- Developers building agents are responsible for implementing appropriate technical controls, disclosing AI generation, testing thoroughly, establishing feedback channels, and obtaining necessary user consents as required by law for

data processing.<sup>88</sup>

- Guardrails and content moderation features can be configured within Copilot Studio to align with responsible AI practices.<sup>82</sup>
- **Compliance:** Copilot Studio, as part of the Microsoft cloud ecosystem, is designed to help organizations meet various compliance requirements, though specific compliance depends on configuration and data sources used.<sup>47</sup>

#### **User Experience (UX) & Interface**

- **Authoring Experience:** Copilot Studio offers a low-code, graphical user interface for building and configuring AI agents. Users can define topics, trigger phrases, conversational flows, and connect to data sources with minimal coding.<sup>80</sup> Natural language can often be used to describe desired agent functionality.<sup>80</sup>
- **Testing and Debugging:** Tools are provided within Copilot Studio for testing agents and debugging actions. 67
- **Analytics and Monitoring:** A built-in analytics dashboard provides insights into agent performance, usage patterns, answer rates, action success rates, and user engagement.<sup>53</sup> Integration with Viva Insights allows for ROI analysis of Copilot Studio agents. 53
- **End-User Interaction:** End-users interact with copilots built in Studio through various channels, including websites, mobile apps, Microsoft Teams, SharePoint, and as extensions to Microsoft 365 Copilot.<sup>60</sup>

# **Open Source Aspects**

While the core Microsoft Copilot Studio platform is a proprietary, commercial product, Microsoft engages with the open-source community and provides tools that facilitate development around its AI ecosystem:

- Microsoft 365 Agents SDK: This is a key offering for developers. It provides libraries and tools (with C#, JavaScript, and Python samples available on GitHub) for building more complex, code-first AI agents. These agents can then interoperate with or be extended by Copilot Studio, bridging the gap between low-code and pro-code development. 55
- **Copilot Studio Samples:** Microsoft maintains a GitHub repository with various samples demonstrating how to build specific features or integrations with Copilot Studio (e.g., Adaptive Card samples, SSO samples, Dataverse Indexer). 59
- **Connectors:** Many Power Platform connectors, which Copilot Studio can leverage, might be based on open standards or have open specifications, facilitating broader interoperability.

# **Availability & Monetization**

Microsoft Copilot Studio is available as a standalone product with a flexible, consumption-based licensing model, and its capabilities are also bundled with Microsoft 365 Copilot licenses for specific use cases.<sup>86</sup>

- **Standalone Licensing Plans:**
	- **Free Trial:** A 30-day free trial is typically available, allowing users to explore the full functionality of Copilot Studio. 90
	- **Pay-as-you-go:** Priced at approximately \$0.01 per message processed by the agent. This offers flexibility for variable usage patterns.<sup>86</sup>
	- **Message Packs:** Organizations can purchase message packs, with a common tier being \$200 per tenant, per month for 25,000 messages. This is suitable for more predictable, higher-volume usage.<sup>86</sup> Overage beyond the pack can be handled by pay-as-you-go. 66
- **Bundling with Microsoft 365 Copilot:**
	- A significant aspect of Copilot Studio's availability is its inclusion with Microsoft 365 Copilot licenses (which cost \$30 per user, per month). Users with an M365 Copilot license can build and use agents within Copilot Studio to extend Microso 365 Copilot experiences (e.g., for use in Teams, SharePoint, M365 Copilot Chat) without incurring additional Copilot Studio message charges for these internal M365 scenarios (classic answers, generative answers, tenant Microsoft Graph grounding are zero-rated).<sup>86</sup> This effectively makes Copilot Studio the customization and extension tool for M365 Copilot for licensed users.
- **Authoring Access:** To build copilots, authors typically need a Copilot Studio user license (which is free) or an active Microsoft 365 Copilot license.<sup>86</sup>
- **Channel Availability:** Agents built with Copilot Studio can be deployed to a wide range of channels, including websites, mobile apps, Microsoft Teams, Facebook, and other third-party messaging platforms (for standalone licenses). For agents built under the M365 Copilot use rights, deployment is focused on Microsoft 365 experiences.<sup>60</sup>

# **Strengths & Weaknesses**

- **Strengths:**
	- **Low-code Accessibility:** Empowers a broader range of users (including citizen developers) to build custom AI conversational agents without extensive coding knowledge. 80
	- **Deep Integration with Microso Ecosystem:** Seamless connections to Microsoft 365 (via Graph), Power Platform (connectors, Power Automate), Dynamics 365, and Azure AI services provide powerful data access and automation capabilities. 53
	- **Extensibility for M365 Copilot:** Key tool for tailoring and extending Microsoft 365 Copilot with enterprise-specific knowledge and processes.<sup>81</sup> The bundling with M365 Copilot licenses is a major adoption driver.
	- **Evolving Agentic Capabilities:** Rapidly advancing features for more autonomous behavior, UI automation ("computer use"), and multi-modal interactions (voice, image). 38
	- **Robust Governance and Security Options:** Features like CMKs, admin controls, and analytics provide enterprise-grade management. 53

#### ● **Weaknesses:**

- **Complexity for Advanced Scenarios:** While low-code is a strength, building highly sophisticated, nuanced agents can still be complex and may require deeper technical expertise, which the M365 Agents SDK aims to address for pro-developers. 94
- **Cost for Standalone External Use:** The per-message pricing for pay-as-you-go or message packs can become costly for high-volume, external-facing agents if not part of the M365 Copilot bundle. 86
- **O** User Interface Perception: Some users find the authoring interface complex or "a typical Microsoft product nightmare," especially when compared to simpler bot-building tools or raw LLM interfaces. 94
- **Base Model Limitations:** Some user feedback suggests that the underlying models used by Copilot Studio (when not directly calling specific Azure OpenAI models) can feel more constrained or less capable in data handling (e.g., context window limits) compared to direct interactions with leading models like raw ChatGPT or Gemini. 94
- **Marketing vs. Reality:** The ease of creating truly advanced and robust agents can sometimes be oversimplified in marketing materials, with practical implementation requiring significant effort in data preparation, topic design, and testing. 94
- **Example 20** *Cloud:* Primarily a cloud-based platform, limiting offline capabilities for the agents themselves. 22

#### **Roadmap & Future Plans**

Microsoft is heavily investing in Copilot Studio, with a clear roadmap towards more powerful and autonomous AI agents. Announcements from Microsoft Build, Ignite, and official release plans indicate the following directions:

- **Enhanced Agent Capabilities:**
	- **Autonomous Agents:** Continued development of agents that can operate independently, responding to events and executing multi-step processes without constant human intervention. 38
	- **Agent Library:** Providing prebuilt agent templates for common scenarios to accelerate development. 38
	- **Computer Use (UI Automation):** Expanding the capabilities of agents to interact with GUIs of desktop and web applications.<sup>53</sup>
	- **Voice and Multimodality:** Improving voice conversation capabilities (IVR integration) and support for image analysis within agents. 38
	- **Deeper Reasoning:** Enhancing the reasoning capabilities of agents. 83
- **Deeper Data Integration and Grounding:**
	- **Azure OpenAI on Your Data:** Enabling agents to use Azure OpenAI models directly on enterprise data for generative answers. 67
	- **Azure AI Search as Knowledge Source:** More robust integration with Azure AI

Search for knowledge retrieval.<sup>38</sup>

- **Example X New Connectors:** Continuously adding new Microsoft Graph connectors and third-party connectors. 37
- **Expanded Knowledge Sources:** Allowing agents to use Teams chats and other real-time knowledge sources. 67
- **AI Model Usage and Flexibility:**
	- **Integration with Azure AI Foundry:** Closer ties to Azure AI Foundry for access to a wider catalog of models (Microsoft, OpenAI, third-party) and custom model management. 38
	- **Bring-Your-Own-Model:** Capabilities to integrate custom models via the Azure AI model catalog. 38
- **Enterprise Governance and Administration:**
	- **Customer Managed Keys (CMKs):** Enhancing data security with customer-controlled encryption keys. 53
	- **Improved Analytics:** More detailed analytics on agent performance, action usage, knowledge source effectiveness, and ROI (via Viva Insights).<sup>53</sup>
	- **Enhanced Security Views and Controls:** Beer visibility and management of agent security within Copilot Studio and the M365 admin center.<sup>35</sup>
	- **Management of Shared Agents:** Admin capabilities to view, search, and block shared Copilot agents. 35
- **Developer Empowerment:**
	- **Microsoft 365 Agents SDK:** Continued development and support for the M365 Agents SDK (C#, JavaScript, Python) to enable pro-developers to build and extend sophisticated agents that can interoperate with Copilot Studio.<sup>38</sup>
	- **Simplied Publishing:** Easier publishing of custom agents and extensions to Microsoft 365 Copilot Chat and other M365 experiences.<sup>39</sup>

Copilot Studio is strategically positioned by Microsoft as the primary tool for democratizing AI application development within the enterprise. Its low-code approach lowers the entry barrier, enabling a wider range of employees to build custom AI solutions.<sup>80</sup> By tightly integrating with Microsoft 365 Copilot and allowing extensions built in Studio to enhance the core M365 AI experience, Microsoft encourages organizations already invested in its productivity suite to adopt Studio for tailoring AI to their specific needs.<sup>67</sup> Furthermore, the platform's ability to connect to a vast array of data sources—Microsoft Graph, Power Platform connectors, Azure AI services—positions Copilot Studio as a central hub for creating enterprise-specific AI agents. This, in turn, deepens customer reliance on the broader Microsoft Cloud ecosystem (Azure, Power Platform, Microsoft 365), creating a powerful flywheel effect for adoption and service consumption.

The evolution of Copilot Studio towards supporting more autonomous and sophisticated agentic behaviors, such as background event processing and UI automation <sup>38</sup>, combined with the parallel development of the M365 Agents SDK for pro-developers<sup>55</sup>, signals a clear ambition. Microsoft is aiming to move beyond simple chatbots and Q&A assistants towards

enabling a more capable "AI workforce." This envisioned AI workforce would consist of a spectrum of agents, from simple task-specific helpers built by business users to complex, deeply integrated autonomous systems developed by programmers, all capable of automating and orchestrating intricate business processes across the enterprise.<sup>3</sup> This strategy aims to deliver substantial productivity gains and transform how work is done within organizations.

# **4. Cross-Cuing Analysis of Microso's AI Ecosystem**

# **4.1. Underlying Technology & AI Models**

Microsoft's AI strategy is characterized by a sophisticated blend of leveraging premier third-party models and developing its own specialized AI technologies, coupled with a significant push towards hybrid AI processing.

- **Leveraging OpenAI vs. Proprietary Models: Microsoft makes extensive use of** OpenAI's advanced models, such as GPT-4 and DALL-E 3, particularly for its powerful cloud-based Copilot experiences like Microsoft 365 Copilot and the AI features in Edge and Bing. <sup>4</sup> This provides immediate access to state-of-the-art generative AI capabilities. Concurrently, Microsoft is heavily investing in its own proprietary models, most notably the Phi family (e.g., Phi-3, Phi Silica).<sup>7</sup> These models are often smaller and more efficient, specifically optimized for on-device execution and targeted tasks, such as Phi Silica for natural language processing within the Windows App SDK on Copilot +  $PCs$ <sup>19</sup> Platforms like Azure AI Studio and Azure AI Foundry further offer a curated catalog of models, including those from Microsoft, OpenAI, and other third parties, providing flexibility for developers.<sup>3</sup> This dual approach—using OpenAI's frontier models for broad, powerful capabilities and developing smaller, specialized models like Phi for efficiency and on-device deployment—allows Microsoft to balance cutting-edge performance with the practical needs of cost, latency, and privacy across diverse scenarios. This strategic diversification ensures access to powerful cloud AI while simultaneously enabling compelling local AI experiences, particularly important for the "AI PC" initiative.
- **The Drive Towards On-Device Processing: NPUs and "AI PCs":** A cornerstone of Microsoft's recent AI strategy is the promotion of "AI PCs," specifically Copilot+ PCs, which are equipped with powerful Neural Processing Units (NPUs) targeting 40+ TOPS.<sup>6</sup> NPUs are specialized accelerators designed for efficient AI workload processing, enabling more complex AI tasks to be performed directly on the device.<sup>6</sup> This shift towards on-device AI aims to deliver improved performance, reduced latency, enhanced user privacy (by keeping data local), and the ability for AI features to function offline.<sup>6</sup> The Windows Copilot Runtime, featuring APIs for on-device models like Phi Silica, Text Recognition, Studio Effects, and the controversial Recall feature, is specifically designed to leverage these NPUs on Copilot+ PCs.<sup>16</sup> DirectML serves as a low-level API for broader GPU and NPU acceleration.<sup>19</sup> This push for NPUs and "AI PCs" is not merely about enabling new features; it represents a strategic effort to alter the economic and

performance dynamics of AI. By facilitating more on-device AI, Microsoft can reduce the reliance on (and associated costs of) cloud compute for certain common AI tasks, while also creating a compelling new hardware upgrade cycle for consumers and enterprises, benefiting both Microsoft and its OEM partners.<sup>6</sup>

- **Balancing Local and Cloud AI Capabilities: Microsoft is actively pursuing a hybrid AI** strategy.<sup>6</sup> While NPUs and Copilot+ PCs enable significant on-device processing for features like Recall, improved local Windows search, and various Windows Copilot functions<sup>9</sup>, complex AI tasks, inference on very large models, and features requiring access to extensive, constantly updated knowledge (such as web-grounded Microso 365 Copilot Chat) continue to rely heavily on cloud-based processing through Azure  $Al.<sup>22</sup>$  The decision to process locally versus in the cloud is influenced by factors such as computational resource availability on the device, data privacy and security requirements, accessibility and collaboration needs, cost implications, and system maintenance considerations. 22
- **User Data for Model Personalization (Enterprise Context):**
	- **Microsoft 365 Copilot:** Microsoft explicitly states that customer data within the M365 environment—including prompts, responses, and data accessed via Microsoft Graph-is not used to train the foundational LLMs that power M365 Copilot. <sup>26</sup> Personalization in this context is achieved through real-time "grounding," where the AI's responses are tailored at the moment of query by accessing the specific user's permitted M365 data and current working context via Microsoft Graph.<sup>33</sup>
	- **Windows Copilot (Personal Accounts):** For users interacting with Windows Copilot using a personal Microsoft account, conversation history can be used for personalization and to improve the underlying AI models, but only if the user explicitly opts in. Users are provided with controls to manage this data and their preferences, including the ability to delete conversation history.<sup>23</sup> Importantly, data from organizational Entra ID accounts is not used for training these general consumer-facing Copilot models. 23
	- *C* **Microsoft Recall:** All data captured by Recall (screen snapshots and the derived index) is stored and processed entirely locally on the user's Copilot+ PC. This data is not sent to Microsoft and is not used for training any of Microsoft's AI models. $^9$

# **4.2. Privacy, Data Handling, and Responsible AI**

Microsoft's approach to AI is underpinned by a commitment to Responsible AI, though its practical application continues to evolve, particularly in response to public and expert feedback.

**•** Microsoft's Stated Principles and Their Application: Microsoft publicly articulates six core principles for Responsible AI: Fairness, Reliability & Safety, Privacy & Security, Inclusiveness, Transparency, and Accountability. <sup>1</sup> These principles are intended to guide the design, development, and deployment of all its AI features, including the various

Copilot offerings. $1$

- $\circ$  For **Microsoft 365 Copilot**, this translates into building with these principles in mind, incorporating protections against harmful content, detecting protected material, and ensuring that the service operates within the established Microso 365 security and compliance boundaries. 40
- The **Microsoft Recall** feature serves as a prominent example of these principles being applied, partly in reaction to initial criticism. The significant privacy backlash following its announcement led to substantial redesigns, including making it strictly opt-in, mandating local encrypted storage, requiring biometric authentication for access, and providing granular user controls—all reflecting an effort to enhance privacy, security, transparency, and user agency.<sup>9</sup>
- $\circ$  For custom copilots built using **Microsoft Copilot Studio**, Microsoft provides guidelines and expects developers to adhere to its AI Code of Conduct and Responsible AI principles.<sup>87</sup> The journey with Recall illustrates that while Microsoft has a framework for Responsible AI, the translation of these principles into complex, data-intensive features can be challenging and may require iterative refinement based on real-world scrutiny and risk assessment. The proactive "Commercial Data Protection" for M365 Copilot<sup>40</sup> demonstrates a more anticipatory approach to enterprise concerns, but the Recall situation highlights the ongoing tension between innovation and perceived privacy risks.
- **Distinctions Between Consumer and Commercial Offerings: A critical aspect of** Microsoft's data handling strategy is the clear differentiation between its consumer-facing and commercial AI offerings:
	- **Commercial Products (e.g., Microso 365 Copilot, Copilot with Commercial Data Protection):** These services come with robust data protection commitments. Crucially, customer data—including prompts, responses, and business data accessed via Microsoft Graph—is not used to train the foundational LLMs.<sup>26</sup> All data processing and storage remain within the customer's Microsoft 365 service boundary, respecting tenant isolation and data residency policies.<sup>40</sup> This approach is designed to meet the stringent privacy and security expectations of enterprise customers.
	- **Consumer Products (e.g., Copilot in Windows/Edge with a personal account, free Copilot services):** For these offerings, conversation history is typically saved by default to enhance user experience. This data **may** be used for personalizing the service and for training the underlying AI models, but only if the user consents or opts in. <sup>23</sup> Users are provided with controls to manage their data, view history, and opt out of data usage for model training or personalization. This bifurcation in data handling policies is a strategic necessity. It allows Microsoft to cater to the different expectations and regulatory landscapes of the consumer and enterprise markets. Commercial clients demand, and receive, assurances that their proprietary data will not be used to improve general AI models, while consumer services can benefit from user data (with consent) to enhance features and

personalization, a common practice in consumer tech. The upcoming enforcement of explicit user consent signals for Microsoft Advertising data originating from the European Economic Area (EEA), UK, and Switzerland by May 5, 2025, further underscores Microsoft's sensitivity to regional data privacy regulations.<sup>99</sup>

- **User Consent Mechanisms Across Products:**
	- **Microsoft Recall:** Requires explicit user opt-in during the Copilot+ PC setup and again to enable the saving of snapshots.<sup>9</sup>
	- **Windows Copilot (Personal):** Users must opt-in for their conversation data to be used for personalization and model training.<sup>23</sup> The upcoming "Hey, Copilot!" voice activation feature will also be opt-in.<sup>12</sup> The planned Settings agent will require user permission before taking actions. 12
	- **Edge Copilot:** Features a user-configurable toggle in settings (Settings > Sidebar > Copilot > Allow Microsoft to access page content) to grant or deny Copilot access to the content of web pages. 76
	- *<b>Microsoft 365 Copilot:* Deployment within an organization is an administrative decision. User consent for data processing is generally covered under the organization's terms of use for Microsoft 365 services. Administrators control the availability of plugins and extensions, and users then choose which of the allowed ones to activate.<sup>40</sup> For specific capabilities like Teams meeting recording and transcription (which Copilot can leverage), administrators can enforce policies requiring explicit consent from participants. 35
	- **Microsoft Advertising Data:** As of May 5, 2025, Microsoft will require advertisers using its tracking tools to obtain and send affirmative opt-in consent signals for website visitors from the EEA, UK, and Switzerland before their data is processed. 99

# **4.3. Integration with User Data**

The depth and method of integration with user data are defining characteristics of Microsoft's various Copilot offerings.

- **Depth of Integration:**
	- **Windows Copilot & Recall:** These features are designed for deep integration with the local Windows environment. Windows Copilot aims to provide contextual understanding based on local data <sup>5</sup>, while Recall goes further by capturing a comprehensive history of on-screen user activity, including files, applications, and websites. 5
	- **Microsoft 365 Copilot:** This service offers profound integration with user data across the entire Microsoft 365 suite. It accesses and reasons over content in OneDrive, SharePoint, Outlook (emails, calendar), and Teams (chats, meetings), among other M365 applications. 33
	- **Edge Copilot:** Integrates with the user's browsing activity, including browsing

history (implicitly for context, though direct access to full history for proactive suggestions is less clear), open tabs, and the content of currently viewed web pages, to provide summaries, answer questions, and offer contextual assistance. 70

**The Centrality of Microsoft Graph:** For Microsoft 365 Copilot, Microsoft Graph is the foundational technology enabling its deep contextual AI capabilities.<sup>33</sup> Microsoft Graph is an API and data fabric that connects and provides access to the vast amount of data generated and stored within an organization's Microsoft 365 services. It understands the relationships between users, their activities, documents, emails, calendar events, chats, meetings, and other organizational entities. By querying Microsoft Graph, M365 Copilot can retrieve the specific information and context needed to ground its LLM responses, making them highly relevant and personalized to the user's current work and organizational environment. <sup>33</sup> This access is governed by the user's existing permissions, ensuring data security and privacy. Furthermore, Microsoft Copilot Studio leverages Graph connectors to extend this data access to custom-built copilots, allowing them to tap into the same rich enterprise context.<sup>35</sup>

The role of Microsoft Graph as the intelligent fabric connecting M365 Copilot to enterprise data is arguably Microsoft's most significant advantage in the workplace AI domain. While LLMs provide the raw generative power, their true utility within an enterprise is unlocked when they can be effectively and securely grounded in the specific, often proprietary, data of that organization. Microsoft Graph provides this crucial grounding layer, enabling M365 Copilot to understand the nuances of a user's projects, communications, and collaborations in a way that a generic AI assistant cannot.<sup>33</sup> This deep, native, and permission-aware integration with an organization's daily operational data fabric is a powerful differentiator against AI tools that lack such inherent connectivity. The ability to further extend this reach via Graph connectors in Copilot Studio only amplifies this strategic asset. $53$

# **4.4. User Experience (UX) & Interface**

Microsoft is working to establish a consistent yet contextually adapted Copilot user experience across its diverse product line.

- **Interaction Models Across the Copilot Ecosystem:**
	- **Windows Copilot:** Typically accessed via a sidebar interface within the OS, a dedicated Copilot keyboard key on newer hardware, the Alt+Spacebar shortcut for quick access, voice commands, and contextual interactions like "Click to Do" on Copilot+ PCs. 5
	- **Example 265 Copilot:** Integrated directly into the user interface of individual Microsoft 365 applications, often appearing in ribbons, task panes, or via contextual prompts. A dedicated Microsoft 365 Copilot Chat interface provides a broader conversational experience. Natural language prompting is the primary interaction method.<sup>33</sup> Copilot Pages offer a collaborative canvas for AI-generated content. 36
	- **Edge Copilot:** Appears as a sidebar in the Edge browser, accessible via a Copilot

icon or by typing @copilot in the address bar. It allows for contextual interaction with web page content, including summarization and Q&A.<sup>70</sup>

● **Common Themes:** Across these implementations, common UX themes include natural language input (both text and increasingly, voice), contextual assistance relevant to the user's current task or content, and an aim for seamless integration into existing user workflows to minimize disruption and maximize productivity.

Microsoft's strategy appears to be the creation of a ubiquitous Copilot presence, aiming for a familiar AI assistant across its ecosystem, while simultaneously tailoring the specific interactions and capabilities to the unique needs and context of each application or environment. The "Copilot" brand and core interaction paradigms (e.g., chat pane, natural language input) are becoming standardized. $8$  However, the data Copilot can access and the actions it can perform differ significantly—for instance, Windows Copilot interacting with local system settings versus M365 Copilot querying enterprise data via Microsoft Graph. A key challenge for Microsoft is to ensure this contextual distinctiveness is clear to the user. Without such clarity, users might misunderstand what data a particular Copilot instance is accessing or what its limitations are, potentially leading to privacy missteps, unmet expectations, or underutilization of features. The introduction of a physical Copilot key on keyboards<sup>27</sup> signals Microsoft's intent to elevate AI interaction to a primary modality for PC users, further emphasizing the need for intuitive and transparent UX design.

# **4.5. Open Source Aspects**

Microsoft is strategically engaging with the open-source community to foster a developer ecosystem around its Copilot platform.

- **Relevant Open-Sourced Components, Models, or SDKs:**
	- **Example 365 Agents SDK:** This SDK, with samples for C#, JavaScript, and Python available on GitHub, enables developers to build custom AI agents. These agents can integrate with Microsoft 365 Copilot, Microsoft Teams, and other platforms, facilitating code-first development of sophisticated agentic solutions. $^{\rm 55}$ The documentation site for this SDK is also open source. 58
	- *C* **Microsoft Copilot Studio Samples:** A collection of samples for Copilot Studio is hosted on GitHub, providing developers with examples and starting points for building custom copilots and extensions. 59
	- **<sup>o</sup> "Build your own copilot Solution Accelerator":** Microsoft offers a solution accelerator on GitHub, including TypeScript, Python, and Bicep components under an MIT license, to help organizations jumpstart the development of their own custom copilot experiences. 101
	- **ONNX Runtime:** The Open Neural Network Exchange (ONNX) Runtime, used for running AI models efficiently across various hardware (including NPUs on Copilot+ PCs), is an open-source project.<sup>16</sup> Microsoft is a key contributor to ONNX.
	- **Phi Models:** While developed within Microsoft Research, there is a trend towards making some versions or aspects of these smaller, efficient language models available to the broader AI community, often through platforms like Azure AI

Studio which provides access to various open models. $^3$  The specific licensing for all variants of Phi models would require detailed checking, but their availability contributes to the open model ecosystem.

○ **Windows Copilot Runtime APIs (DirectML, WebNN):** These APIs, such as DirectML (part of DirectX) and WebNN (a W3C standard in development), allow developers to tap into hardware acceleration for AI tasks on Windows devices. While the APIs are specifications, their implementations are part of Windows, but their open nature encourages broad adoption. 19

Microsoft's open-source contributions, particularly in the form of SDKs like the M365 Agents SDK<sup>58</sup> and solution accelerators<sup>101</sup>, are not merely altruistic. They represent a strategic initiative to cultivate a vibrant developer ecosystem around its Copilot platform. By providing these tools and resources, Microsoft lowers the barrier to entry for developers seeking to build custom AI solutions that integrate with or extend Microsoft's core AI offerings. This encourages third-party innovation, which can address niche use cases and specialized industry needs that Microsoft itself might not prioritize. Such an ecosystem drives broader adoption of Microsoft's AI technologies, attracts developer talent, and strengthens Microsoft's competitive position in the rapidly evolving AI landscape.

# **4.6. Availability & Monetization**

Microsoft employs a multi-tiered strategy for the availability and monetization of its Copilot features, balancing broad accessibility with premium offerings.

- **OS Integration and Free Services:**
	- **Windows Copilot:** Basic AI assistance features are integrated into Windows 10 (compatible versions) and Windows 11 at no additional cost to the user. <sup>4</sup> More advanced on-device AI features, such as Recall, are bundled with the purchase of new Copilot+ PC hardware and are not separate subscriptions.<sup>9</sup>
	- **Edge Copilot:** Core AI features within the Microsoft Edge browser, such as page summarization and contextual Q&A, are provided free of charge.<sup>13</sup>
- **Premium Subscriptions and Add-ons:**
	- **Copilot Pro:** A consumer-focused subscription priced at \$20 per user, per month. It offers benefits like priority access to newer and more powerful LLMs (e.g., GPT-4 Turbo during peak times), faster image generation with more daily "boosts," and integration of Copilot AI features into Microsoft 365 Personal and Family applications (Word, Excel, PowerPoint, Outlook). <sup>4</sup> Some upcoming Edge Copilot features, like "Copilot Actions," will also be exclusive to Pro subscribers. 70
	- *O* **Microsoft 365 Copilot (Enterprise):** This is an add-on license for qualifying Microsoft 365 commercial subscriptions (e.g., Microsoft 365 E3/E5, Business Standard/Premium). It is priced at \$30 per user, per month, typically requiring an annual commitment.<sup>49</sup> This unlocks the full suite of AI-powered productivity features within the Microsoft 365 apps and services for business users.
	- **Microsoft Copilot Studio:** This platform for building custom AI agents has a tiered licensing model:
- A free trial is available.<sup>90</sup>
- **Pay-as-you-go** option at \$0.01 per message for standalone agents.<sup>86</sup>
- **Message packs** (e.g., \$200 per month for 25,000 messages) for predictable, higher-volume needs. 86
- Crucially, Microsoft 365 Copilot licenses include use rights for Copilot **Studio** when building agents that extend M365 Copilot for internal use within Teams, SharePoint, and M365 Copilot Chat, with message consumption for these scenarios often being zero-rated or unlimited within the M365 Copilot license. 86

Microsoft's monetization strategy for its Copilot ecosystem is carefully constructed to achieve multiple objectives. The provision of free, integrated AI features in Windows<sup>5</sup> and Edge<sup>71</sup> serves as a significant value-add, aiming to drive user adoption and loyalty to these core Microsoft platforms. Simultaneously, Microsoft targets distinct market segments for premium revenue generation. Copilot Pro <sup>13</sup> caters to individual consumers and power users willing to pay for enhanced AI capabilities and integration with personal M365 apps. Microsoft 365 Copilot<sup>49</sup> represents a major enterprise revenue stream, with its pricing justified by the promise of substantial productivity gains and efficiency improvements for businesses.<sup>57</sup> Copilot Studio's flexible licensing <sup>86</sup>, including its bundled value within the M365 Copilot license for internal extensions, encourages enterprises to customize and deepen their AI investments within the Microsoft ecosystem, while also providing a path for monetizing standalone or external-facing custom agents. This multi-faceted approach allows Microsoft to maximize the reach of its AI technologies while creating diverse and scalable revenue opportunities.

# **5. Strategic Assessment and Outlook**

# **5.1. Identied Strengths**

Microsoft's AI initiatives exhibit several key strengths:

- **Deep OS and Productivity Suite Integration:** Microsoft possesses an unparalleled advantage in its ability to deeply embed AI functionalities across the Windows operating system and the widely adopted Microsoft 365 productivity suite. This means AI assistance is available directly within the environments where users conduct most of their daily work. 5
- **Enterprise Footprint and Trust:** With a strong, long-standing presence in the enterprise sector, Microsoft has built significant trust regarding security, privacy, and compliance. The "Commercial Data Protection" commitment for Microsoft 365 Copilot is a testament to this focus, addressing key enterprise concerns about data handling.<sup>28</sup>
- **Robust Azure AI Backend:** The power and scalability of Microsoft's Azure cloud platform, including Azure OpenAI Service, Azure AI Studio, and Azure AI Foundry, provide a formidable backend infrastructure to develop, deploy, and manage sophisticated Copilot experiences at scale.<sup>3</sup>
- **Hybrid AI Approach (Cloud + On-Device):** Strategic investments in both cloud-based AI and on-device AI capabilities (through NPUs and "AI PCs") offer flexibility. This allows Microsoft to optimize for performance, privacy, cost, and offline functionality depending on the specific use case and device capabilities.<sup>6</sup>
- **Growing Developer Ecosystem:** Tools like Microsoft Copilot Studio and the Microsoft 365 Agents SDK are fostering a developer community, enabling customization, extension, and the creation of bespoke AI solutions that integrate with the Copilot platform.<sup>53</sup>

# **5.2. Identied Weaknesses & Challenges**

Despite its strengths, Microsoft faces several challenges:

- **Reliance on Cloud for Complex Tasks:** Many of the most advanced AI features, particularly those involving large language models or extensive real-time data access, still necessitate cloud connectivity and processing. This can introduce latency, incur operational costs, and limit offline usability for certain functionalities.<sup>13</sup>
- **Privacy Perceptions and User Trust:** Features that involve extensive data collection or monitoring, such as Microsoft Recall, have encountered significant public and expert scrutiny regarding privacy, even with robust technical safeguards like local processing and opt-in mechanisms. Overcoming these perception challenges and maintaining user trust is
