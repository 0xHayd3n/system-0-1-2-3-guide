# Concepts and context

This module reads **Taniguchi et al., arXiv:2503.06138v3, 16 July 2025** as a proposed framework for organizing cognition. Its central move is to widen the unit of explanation: intelligent behavior involves an organism's physical coupling to its environment, individual cognition, and the evolving symbolic practices of groups. The paper brings these domains together; it does not report a new experiment establishing a four-process architecture. All page references below use one-based PDF pages.

## The problem the framework addresses

Dual-process theory distinguishes relatively automatic, intuitive processing from relatively deliberative processing. The authors argue that this familiar System 1/System 2 contrast leaves two important sources of adaptation underdescribed: the body can contribute useful behavior before explicit neural calculation, and communities can change the symbols through which individuals think and cooperate. They also seek a temporal account broad enough to connect these processes. These are the paper's motivations, rather than demonstrated failures of every existing dual-process model. [§1, PDF pp.3–5](https://arxiv.org/pdf/2503.06138v3#page=3)

The proposed extension adds **System 0**, bodily and environmental dynamics that support adaptation, and **System 3**, collective processes that produce and reshape shared symbols. The numbering indicates the authors' conceptual hierarchy, not four pieces of software that must be installed separately. Figure 3 places physical, implicit, internal explicit, and external symbolic organization in relation to one another. Reading the hierarchy as a one-way pipeline would miss the feedback from social practices to individuals and from embodiment to what agents can perceive and do. [§3.1, Figure 3, PDF pp.15–17](https://arxiv.org/pdf/2503.06138v3#page=15)

## Four background traditions

### Dual-process ideas in AI

Section 2.1.1 uses the contrast between symbolic reasoning and learned pattern recognition as an entry point. It then complicates that contrast: deliberative behavior can be assembled from learned components, while representations need enough structure to support recombination and transfer. The discussion connects disentanglement, attention, recurrent independent mechanisms, and learned program primitives to this problem. The authors cite prior research here; these are not methods introduced or benchmarked in this paper. [§2.1.1, PDF pp.5–6](https://arxiv.org/pdf/2503.06138v3#page=5)

The same section discusses stepwise prompting, search over reasoning paths, self-revision, memory of previous attempts, tool use, and agents that repeatedly act in an environment. These examples motivate calling some LLM workflows “System 2-like.” That resemblance does not establish a human cognitive mechanism inside a language model. It also does not imply that producing more intermediate text makes an answer correct. The source offers a conceptual connection across existing approaches. [§2.1.1, PDF pp.6–8](https://arxiv.org/pdf/2503.06138v3#page=6)

### Neurodynamics and embodied cognition

Section 2.1.2 supplies a different route to fast and slow organization: recurrent networks with different update dynamics can organize rapid sensorimotor patterns and slower combinations of those patterns. Top-down predictions and bottom-up errors couple the levels. Section 2.2 then moves below neural processing to morphology, compliance, passive dynamics, and physical reservoir computing. These strands make embodiment part of the explanation rather than merely an input to a disembodied reasoner. The next module examines their examples and boundaries. [§§2.1.2–2.2, Figures 1–2, PDF pp.8–11](https://arxiv.org/pdf/2503.06138v3#page=8)

### Multi-agent systems and emergent language

Section 2.3 distinguishes systems that collaborate **using an already available language** from research on **how communication conventions arise and change**. Voting, debate, model fusion, and simulated societies illustrate the first direction. Emergent communication, emergent language, and symbol emergence motivate the second. The paper's stronger interest is the adaptability of the symbolic medium itself: a society can revise categories, meanings, and rules through decentralized interaction. [§2.3, PDF pp.12–13](https://arxiv.org/pdf/2503.06138v3#page=12)

This is where collective predictive coding (CPC), attributed to Taniguchi's earlier work, enters. CPC interprets shared symbolic organization through decentralized inference. The present paper uses that hypothesis within a larger quad-process synthesis. It should not receive credit for inventing every component it combines, nor should a citation to earlier naming-game studies be presented as a new empirical validation of System 3. [§1, PDF p.4](https://arxiv.org/pdf/2503.06138v3#page=4), [§2.3, PDF p.13](https://arxiv.org/pdf/2503.06138v3#page=13)

### Bergson and intrinsic timescales

Section 2.4 introduces the authors' multi-timescale reading of Bergson. A process has a characteristic temporal organization: physical change, sensorimotor engagement, recollection, and social adaptation need not share one rhythm. The “window of the present” concerns the span within which ongoing change is integrated into experience. Automatic and attentive recognition supply a bridge to the fast/slow distinction. The extended framework in §4 develops this philosophical interpretation further. [§2.4, PDF pp.13–15](https://arxiv.org/pdf/2503.06138v3#page=13)

Treat the historical timing examples in this discussion as cited background, not experimentally determined thresholds separating Systems 0–3. “Super-fast” and “super-slow” are relative descriptions; the framework does not assign a universal number of milliseconds or years to each system.

## Glossary

| Term | Working meaning in this guide | Source |
| --- | --- | --- |
| System 0 | Adaptive bodily/environmental dynamics before explicit neural computation | [§§2.2, 3.1, PDF pp.10–11, 15–16](https://arxiv.org/pdf/2503.06138v3#page=10) |
| System 1 | Relatively fast, intuitive processing and implicit organization | [§3.3, PDF p.20](https://arxiv.org/pdf/2503.06138v3#page=20) |
| System 2 | Relatively slow, deliberative processing involving explicit internal organization | [§3.3, PDF pp.20–21](https://arxiv.org/pdf/2503.06138v3#page=20) |
| System 3 | Collective organization through shared, evolving symbols | [§§3.1–3.2, PDF pp.16–19](https://arxiv.org/pdf/2503.06138v3#page=16) |
| Morphological computation | A body's physical properties and environmental interaction contribute computational or control functions | [§2.2, PDF pp.10–11](https://arxiv.org/pdf/2503.06138v3#page=10) |
| Semiotic plasticity | Adaptability of sign systems and their relationships to what they express | [§1, PDF p.4; §3.2, PDF p.19](https://arxiv.org/pdf/2503.06138v3#page=19) |
| CPC | Collective predictive coding: a hypothesis about decentralized inference and symbol emergence | [§3.2, PDF pp.17–19](https://arxiv.org/pdf/2503.06138v3#page=17) |
| Motor memory | Habits and skills; extended in §4 to prior organization that makes later action easier | [§§4.2–4.3, PDF pp.23–25](https://arxiv.org/pdf/2503.06138v3#page=23) |
| Pure memory | Retained particular experiences that can support reconstruction beyond an established routine | [§4.2, PDF pp.23–24](https://arxiv.org/pdf/2503.06138v3#page=23) |
| Canalization | Formation of a landscape of possibilities that channels subsequent behavior | [§4.3, PDF pp.24–25](https://arxiv.org/pdf/2503.06138v3#page=24) |

## Reading questions

1. What explanatory work does adding a bodily level accomplish beyond describing a faster neural controller?
2. How would adapting a shared symbol differ from learning to use a fixed label more accurately?
3. Which links in the paper are mathematical hypotheses, historical interpretations, or analogies between research traditions?
4. What observation could distinguish the quad-process account from an alternative explanation of the same behavior?

Continue with [embodiment and individual cognition](02-embodiment-and-individual-cognition.md), or return to the [reading routes](../README.md).
