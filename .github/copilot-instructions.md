Project Goal

Build ml-notes.akkefa.com as a first-principles PyTorch learning lab.

This site must explain deep learning and PyTorch through:
	•	math intuition
	•	formal math with LaTeX
	•	manual PyTorch tensor implementation
	•	verification against tiny hand-worked examples
	•	comparison with official PyTorch APIs
	•	practical engineering usage
	•	selective internal/system-level notes

The site is not a generic PyTorch docs clone.
It is a structured educational system for mastering PyTorch deeply.

⸻

Core Product Definition

The site should answer this question on every major topic:

How does this concept work mathematically, how do I implement it manually using PyTorch tensors, how do I verify it, how does PyTorch expose it officially, and what is happening behind the scenes?

⸻

Writing Philosophy

All content must follow these principles:
	1.	Manual first, built-in second
	•	First explain the concept.
	•	Then show the math.
	•	Then implement using raw tensor operations.
	•	Then verify with a tiny numerical example.
	•	Then compare against the PyTorch built-in API.
	2.	Math must be attached to implementation
	•	Never explain formulas in isolation.
	•	Always connect formulas to tensor shapes, operations, and gradients.
	3.	Every page must teach deeply, not superficially
	•	Avoid shallow API-only pages.
	•	Avoid long text without examples.
	•	Avoid unexplained code.
	4.	Internal details should be layered
	•	Begin with Python-side intuition.
	•	Then tensor/autograd behavior.
	•	Then system/backend notes.
	•	Only introduce dispatcher, ATen, C++, CUDA, or torch.compile when contextually useful.
	5.	The site must feel like a guided system
	•	It should not feel like scattered notes.
	•	It should feel like a deliberate roadmap from basics to advanced mastery.

⸻

Tone and Writing Style

Use these style rules for all writing:
	•	Explain in clean, simple English.
	•	Be precise but not unnecessarily academic.
	•	Avoid overusing jargon.
	•	Do not assume the reader understands hidden details.
	•	Explain shape transitions explicitly.
	•	Show tiny examples before large abstractions.
	•	Use LaTeX for important formulas.
	•	Prefer short paragraphs and structured headings.
	•	Always connect theory to code.
	•	Always connect code to tensor shapes.

⸻

Copilot Behavior Guidelines

When helping with this project, Copilot should:
	•	preserve the first-principles structure
	•	avoid generating shallow filler content
	•	suggest smaller, focused pages instead of giant pages
	•	keep explanations tied to math and tensor operations
	•	help generate LaTeX where needed
	•	maintain consistency in filenames, headings, and navigation structure

Copilot should not:
	•	turn this site into a generic docs mirror
	•	overcomplicate early beginner pages with unnecessary internals
	•	generate vague motivational text instead of real technical content


