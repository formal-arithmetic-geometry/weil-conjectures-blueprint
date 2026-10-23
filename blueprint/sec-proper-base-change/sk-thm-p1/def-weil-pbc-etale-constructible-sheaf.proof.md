+++
kind = "proof"
of = "def-weil-pbc-etale-constructible-sheaf"
uses = ["def-constructible-locally-constant", "def-constructible-stratification", "def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "def-weil-pbc-inverse-image"]
+++
(Data: the strata.) A stratification $(\iota_k:Z_k\to T)_{k<n}$ of the scheme $T$ in the sense of [def-constructible-stratification] is a finite family of pairwise disjoint locally closed subsets $T_k$ covering $T$ and immersions $\iota_k$ with image $T_k$. Condition (a) asks each $T_k$ to be a constructible subset of $|T|$; this is what distinguishes the notion from [def-constructible-constructible], whose strata are only locally closed.

(The restriction to a stratum.) For each $k$ the inverse image functor along $\iota_k$ [def-weil-pbc-inverse-image] sends the sheaf of $\Lambda_T$-modules $\mathcal F$ [def-weil-pbc-etale-sheaves] to a sheaf of $\Lambda_{Z_k}$-modules on $(Z_k)_{\Et}$ [def-weil-pbc-etale-site], since the constant coefficient ring pulls back to itself.

(The condition on a stratum.) Condition (b) is local constancy as a sheaf of $\Lambda$-modules [def-constructible-locally-constant], together with the requirement that each geometric stalk, a $\Lambda$-module, be finitely generated. Both conditions are invariant under isomorphism of sheaves, so constructibility is a property of $\mathcal F$.
