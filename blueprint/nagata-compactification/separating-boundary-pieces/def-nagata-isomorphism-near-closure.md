+++
id = "def-nagata-isomorphism-near-closure"
kind = "definition"
title = "Modification making a proper map an isomorphism near a closure"
order = 398
lean = ["AlgebraicGeometry.exists_admissibleBlowup_isIso_strictTransformMap_near_closure"]
uses = ["def-nagata-elimination-indeterminacy", "def-nagata-extended-admissible-blowup", "def-nagata-maximal-isomorphism-open", "def-nagata-separate-constructible-closed", "def-nagata-spectral-constructible-separation"]
+++
Let $X$ be qcqs, let $q\colon Z\to X$ be proper, let $V\subseteq X$ be a
quasi-compact open, set
$U=q^{-1}(V)$, and let $T\subseteq V$ be closed. Assume $U\to V$ is an
isomorphism over an open neighbourhood of $T$. Let $E\subseteq V$ be
the complement of $\operatorname{IsoOpen}(U\to V)$ from
[def-nagata-maximal-isomorphism-open].
Apply [def-nagata-spectral-constructible-separation] to $(T,E)$ and
denote the output by $(T_c,E_c)$. Perform the explicitly constructed
$V$-admissible separation blow-up

$$
X_1=\mathsf{CSepBl}_V(T_c,E_c).
$$

Let $\overline E_c$ denote the topological closure of the underlying subset
of $E_c$ in $X_1$, and let
$X_0=X_1\setminus\overline E_c$ and let $q_0\colon Z_0\to X_0$ be the
restriction of the strict transform of $q$. Form
$X_0^{\mathrm{el}}(q_0,V\setminus E_c)$ and extend this admissible blow-up
to $X_1$ by [def-nagata-extended-admissible-blowup]. Define
$\mathsf{IsoBl}_{V,T}(q)\to X$ to be the composite of these two
$V$-admissible blow-ups, represented as one blow-up by the composition
construction.
