+++
kind = "proof"
of = "lem-weil-pbc-finite-pushforward-open-quotient-constant"
uses = ["lem-fin-extension-by-zero", "lem-weil-pbc-finite-pushforward-constructible-noetherian"]
+++
Y is Noetherian since it is finite over X. The constant quotient module sheaf is finite locally constant since Λ/(ℓ) is cyclic. Extension by zero along the quasi-compact open immersion preserves constructibility. ([lem-fin-extension-by-zero]).

Apply finite pushforward constructibility to the underlying finite abelian sheaf. The resulting sheaf remains killed by ℓ. Its module operations factor through the finite ring R, so on each finite-set constant stratum a refinement trivializes the finitely many R-operations. The resulting finite constant R-modules are finitely generated over Λ. This yields the required constructible module sheaf; no Noetherian ring assumption on Λ is used. ([lem-weil-pbc-finite-pushforward-constructible-noetherian]).
