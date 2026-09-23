+++
id = "lem-weil-pbc-degree-zero-strict-henselian"
kind = "lemma"
title = "Degree-zero comparison over a strictly henselian base"
order = 1259
uses = ["def-weil-pbc-etale-site", "def-weil-pbc-henselian-terminology", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-etale-degree-zero", "lem-weil-pbc-finite-pullback-identities", "lem-weil-pbc-finite-refinement-etale-cover", "lem-weil-pbc-spectral-restriction", "lem-weil-pbc-universal-homeomorphism-base-change", "thm-weil-pbc-stein-connectedness", "thm-weil-pbc-universal-homeomorphism-invariance"]
+++
Let $A$ be strictly henselian local
[def-weil-pbc-henselian-terminology], let $S=\operatorname{Spec}A$, and write
$k=A/\mathfrak m$. Let $s$ be the *canonical closed geometric point*
$s:\Spec k^{\mathrm{alg}}\to S$ with $k^{\mathrm{alg}}$ an algebraic closure
of $k$ (the convention of this statement: only in this normalization is the
comparison below canonical; a geometric point with transcendental field of
constants gives genuinely larger sections for general etale sheaves, e.g. for
$F=\mathbf G_m$, so it is not used), and let $p:Z\to S$ be proper
[def-weil-pbc-scheme-conventions]. For every etale sheaf $F$ on the small
etale site [def-weil-pbc-etale-site] of $Z$, restriction gives

$$
 \Gamma(Z,F)\xrightarrow{\sim}\Gamma(Z_s,F|_{Z_s}),
 \qquad\text{equivalently}\quad
 \Gamma(Z,F)\xrightarrow{\sim}\Gamma(Z_0,F|_{Z_0})
$$

with $Z_0=Z\times_S\Spec k$ (the identification of $Z_s$ with $Z_0$ being the
universal homeomorphism of the proof). This isomorphism is natural in $F$ and
in finite pullback over $S$.

## Proof

Write $k=A/\mathfrak m$ and $Z_0=Z\times_SS_0$ with $S_0=\Spec k$, so that
$Z_0\subset Z$ is the closed member of the pair $(\mathfrak m)$. The proof
has four steps.

*Step 1: the geometric fiber and the closed fiber agree.* By
[def-weil-pbc-henselian-terminology] a strictly henselian local ring is
henselian local, so $(A,\mathfrak m)$ is a henselian pair, and its residue
field $k$ is separably closed. The closed geometric point $s$ is a geometric
point lying over $S_0$; we take it in the standard normalization, $s:\Spec
k^{\mathrm{alg}}\to S$ with $k^{\mathrm{alg}}$ the algebraic closure of $k$
(any other geometric point over the same closed point of $S_0$ with
transcendental field of constants would give a different statement for
general etale sheaves, e.g. for $F=\mathbf G_m$ on a point, so the comparison
below is the one for the canonical choice; this is the convention of the
Stacks Project comparison, Tag
[0A0C](https://stacks.math.columbia.edu/tag/0A0C), which is stated for the
closed member of the henselian pair, and the geometric-point formulation
below is only the transport of that statement). Since $k$ is separably
closed, every element of $k^{\mathrm{alg}}$ is purely inseparable over $k$
(the separable closure of $k$ is $k$ itself), so $\Spec k^{\mathrm{alg}}\to
\Spec k$ is a universal homeomorphism (it is surjective, integral, and
radicial); base changes of universal homeomorphisms are universal
homeomorphisms ([lem-weil-pbc-universal-homeomorphism-base-change]), hence
$Z_s=Z\times_S\Spec k^{\mathrm{alg}}\to Z_0$ is one. By
[thm-weil-pbc-universal-homeomorphism-invariance] the small etale sites of
$Z_s$ and $Z_0$ are corresponding, carrying $F|_{Z_0}$ to $F|_{Z_s}$, so
$\Gamma(Z_s,F|_{Z_s})=\Gamma(Z_0,F|_{Z_0})$ canonically. It is therefore
enough to compute $\Gamma(Z_0,F|_{Z_0})$.

*Step 2: apply the henselian-pair comparison* (this is Stacks Project, Tag
[0A0C](https://stacks.math.columbia.edu/tag/0A0C), Lemma 59.91.2). The two
hypotheses of [lem-weil-pbc-etale-degree-zero] hold verbatim: $(A,\mathfrak
m)$ is a henselian pair by Step 1, and $p:Z\to S$ is proper by hypothesis.
Its conclusion: for every etale abelian sheaf $F$ on $Z$ the restriction map

$$
 \Gamma(Z,F)\xrightarrow{\sim}\Gamma(Z_0,F|_{Z_0})
$$

is an isomorphism. With the identification of Step 1 this is the asserted
isomorphism $\Gamma(Z,F)\xrightarrow{\sim}\Gamma(Z_s,F|_{Z_s})$.

*Step 3: the content of the cited comparison.* It is useful to see where
[lem-weil-pbc-etale-degree-zero] gets its statement, since its hypotheses
coincide with the present ones. In Stage 1 of its proof, the connectedness
conclusion of [thm-weil-pbc-stein-connectedness] (applied to the proper $Z\to
S$), together with the spectrality of $Z$ and closedness of $Z_0\subset Z$
(as in [def-weil-pbc-scheme-conventions], since $Z$ is proper over the affine
$S$), is the hypothesis of [lem-weil-pbc-spectral-restriction], which then
identifies sections of every locally constant
[def-weil-pbc-etale-sheaves] Zariski sheaf on $Z$ with its sections on $Z_0$;
the extension of this identification to the constructible sheaf actually used
is the open item recorded in the status note to
[thm-weil-pbc-stein-connectedness]. In Stage 2 the finite refinements of
[lem-weil-pbc-finite-refinement-etale-cover], together with
[lem-weil-pbc-finite-pullback-identities], carry an etale section from a
neighbourhood of $Z_0$ to the finite covers of $Z$ on which Stage 1 applies,
producing an etale section of $F$ with prescribed restriction. Thus the two
stages constitute exactly the comparison of Step 2, and no other input is
used.

*Step 4: naturality and finite pullback.* The comparison is natural in $F$:
the identification of Step 1 and both stages of Step 3 are functorial in the
sheaf. It is natural in finite pullback over $S$. Let $h:Z'\to Z$ be finite.
The composite $Z'\to S$ is proper (the composite of the proper $h$, as finite
morphisms are proper, with the proper $p$), so
[lem-weil-pbc-etale-degree-zero] applies to $Z'$ as well and gives the
comparison for $\Gamma(Z',h^{-1}F)$; by the naturality in finite pullback
recorded in [lem-weil-pbc-etale-degree-zero] (and transported through the
identifications of Step 1), the comparison for $Z$, the comparison for $Z'$,
and the finite pullbacks form a commutative square. This proves the
assertion.
