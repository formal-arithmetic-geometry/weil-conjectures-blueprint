+++
id = "def-nagata-global-blowup-glue-data"
kind = "definition"
title = "Raw global blow-up gluing datum"
order = 54
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.blowupGluingData", "AlgebraicGeometry.Scheme.IdealSheafData.blowupNatTrans_equifibered"]
uses = ["def-nagata-affine-blowup", "def-nagata-affine-blowup-restriction-map", "def-nagata-affine-proj", "def-nagata-global-blowup-local-model", "def-nagata-global-blowup-overlap-basic-map", "def-nagata-homogeneous-localization-degree-zero", "def-nagata-rees-algebra", "def-nagata-rees-localization-map", "def-nagata-rees-piece", "lemma-nagata-global-blowup-overlap-basic", "lemma-nagata-global-blowup-overlap-cocycle", "lemma-nagata-global-blowup-overlap-id-symm", "lemma-nagata-global-blowup-overlap-independent", "lemma-nagata-localization-ideal-pow", "lemma-nagata-rees-degree-zero", "lemma-nagata-rees-piece-membership", "lemma-nagata-rees-piece-mul", "prop-nagata-rees-graded"]
+++
Let $\mathcal I\subseteq\mathcal O_X$ be a quasi-coherent ideal. Define
$\mathsf G(X,\mathcal I)$ to be the relative gluing datum over $X$,
indexed by the set of all affine opens of $X$ ordered by inclusion,
consisting of the diagram $V\mapsto\mathsf B_V(\mathcal I)$ of
[def-nagata-global-blowup-local-model] together with the structure
morphisms $\mathsf B_V(\mathcal I)\to V$. These structure morphisms are
compatible with the transition maps, and for all affine opens
$W\subseteq V$ the square

$$
\begin{array}{ccc}
\mathsf B_W(\mathcal I) & \longrightarrow & \mathsf B_V(\mathcal I)\\
\downarrow & & \downarrow\\
W & \longrightarrow & V
\end{array}
$$

is cartesian.

## Proof

For affine opens $W\subseteq V$, the transition map
$\mathsf B_W(\mathcal I)\to\mathsf B_V(\mathcal I)$ is induced by the
restriction $A_V\to A_W$, and the structure morphisms are induced by the
degree-zero maps $A_V\to\mathcal R_{A_V}(I_V)_0$ and
$A_W\to\mathcal R_{A_W}(I_W)_0$. The coefficientwise map of Rees algebras
restricts in degree zero to $A_V\to A_W$, so the structure morphisms are
compatible with the transition maps and with the inclusion $W\subseteq V$.

If $W$ is a basic open $D(s)$ of $V$, the square is cartesian by
[lemma-nagata-global-blowup-overlap-basic]. For general affine opens
$W\subseteq V$, cover $W$ by opens $W'$ that are basic opens both of $W$
and of $V$ (any point of $W$ has such a neighbourhood: take a basic open of
$V$ inside $W$; it is then also a basic open of $W$). By the basic case
applied to $W'\subseteq W$ and to $W'\subseteq V$, and since the transition
maps compose (the diagram is a functor), both
$\mathsf B_W(\mathcal I)$ and $\mathsf B_V(\mathcal I)\times_VW$ restrict
over $W'$ to $\mathsf B_{W'}(\mathcal I)$, compatibly with the canonical
morphism $\mathsf B_W(\mathcal I)\to\mathsf B_V(\mathcal I)\times_VW$.
Hence this morphism over $W$ is an isomorphism over every $W'$ of a cover
of $W$, so it is an isomorphism, and the square is cartesian.
