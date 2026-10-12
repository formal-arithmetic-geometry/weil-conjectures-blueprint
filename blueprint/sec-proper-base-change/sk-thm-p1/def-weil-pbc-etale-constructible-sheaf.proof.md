+++
kind = "proof"
of = "def-weil-pbc-etale-constructible-sheaf"
uses = ["def-constructible-locally-constant", "def-constructible-stratification", "def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "def-weil-pbc-inverse-image"]
+++
(Data: the strata.) A stratification $(\iota_k:Z_k\to T)_{k<n}$ of the scheme $T$ in the sense of [def-constructible-stratification]: a finite family of pairwise disjoint locally closed subsets $T_k$ covering $T$ and immersions $\iota_k$ with image $T_k$. Condition (a) asks each $T_k$ to be a constructible subset of $|T|$ `Topology.IsConstructible` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Topology/Constructible.lean)) (Mathlib's Topology.IsConstructible); this is what distinguishes the notion from [def-constructible-constructible], whose strata are only locally closed.

(The restriction to a stratum.) For each $k$ the inverse image functor along $\iota_k$ [def-weil-pbc-inverse-image] sends the sheaf of $\Lambda_T$-modules $\mathcal F$ [def-weil-pbc-etale-sheaves] to a sheaf of $\Lambda_{Z_k}$-modules on $(Z_k)_{\Et}$ [def-weil-pbc-etale-site] (the coefficient ring pulls back to itself, as recorded in [def-weil-pbc-inverse-image]); this is the '$\mathcal F|_{X_i}$' of Stacks.

(The condition on a stratum.) Condition (b) is local constancy as a sheaf of $\Lambda$-modules [def-constructible-locally-constant] (coefficient category the $\Lambda$-modules), with all constant values $M_i$ finite $\Lambda$-modules: Stacks 03RU's 'finite locally constant' (finite values). That this is the same as [def-constructible-finite-locally-constant] for $\Lambda$-modules (locally constant with finite geometric stalks, the Lean IsFiniteLocallyConstantSheaf) and as Stacks 03RW(3)'s 'of finite type and locally constant' is the pointer lem-weil-pbc-finite-locally-constant-module-values, not part of the definition.
