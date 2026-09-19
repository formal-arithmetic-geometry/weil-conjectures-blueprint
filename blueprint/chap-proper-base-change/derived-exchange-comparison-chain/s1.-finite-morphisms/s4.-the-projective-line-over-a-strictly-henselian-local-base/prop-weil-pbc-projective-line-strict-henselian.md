+++
id = "prop-weil-pbc-projective-line-strict-henselian"
kind = "theorem"
title = "Strict-henselian projective-line proper base change"
order = 714
tags = ["latex:proposition"]
uses = ["prop-weil-pbc-p1-strict-henselian-comparison"]
+++
Let $A\to B$ be a local map of strictly henselian local rings which induces
an isomorphism of their separably closed residue fields. For the Cartesian
square obtained from $\mathbf P^1_A\to\operatorname{Spec}A$, the derived
exchange map for a torsion sheaf is an isomorphism on the stalk at the closed
geometric point of $\operatorname{Spec}B$.

## Proof

Write $S=\operatorname{Spec}A$, $T=\operatorname{Spec}B$, and let
$\bar t$ and $\bar s$ be their closed geometric points under the chosen
residue-field identification. Choose an injective resolution
$F\to I^\bullet$ on $\mathbf P^1_A$. A strict henselian local scheme is
initial in the opposite category of pointed etale neighbourhoods of its
closed geometric point: the chosen point selects a unique section of the
connected component of any pointed etale neighbourhood. Consequently the
pointed-neighbourhood stalk colimit has canonical restriction quasi-isomorphisms to global
cohomology, and the following rectangle is defined degree by degree:

$$
\begin{CD}
(Rp_*F)_{\bar s} @>{(\operatorname{Ex}_{\square,F})_{\bar t}}>>
(Rp_{T,*}F_T)_{\bar t}\\
@V{\Phi_A}V{\sim}V @VV{\Phi_B}V\\
R\Gamma(\mathbf P^1_A,F) @>{\operatorname{res}_{A,B}}>>
R\Gamma(\mathbf P^1_B,F_T)\\
@V{\rho_A}V{\sim}V @VV{\rho_B}V{\sim}V\\
R\Gamma(\mathbf P^1_{k_A},F_{k_A}) @>{\operatorname{id}}>>
R\Gamma(\mathbf P^1_{k_B},F_{k_B}).
\end{CD}
$$

Here $\Phi_A$ and $\Phi_B$ send a germ represented on a pointed
neighbourhood to its pullback on the corresponding strict local base. To
verify that they are quasi-isomorphisms without a stalk theorem as a leaf,
compute a cohomology class on a finite split etale hypercover. Its
$(q+1)$-skeleton, its cocycle, and any null-homotopy contain finitely many
etale objects, face maps, sections, and equalities. The unique pointed
sections pull this complete finite datum to the strict local base; conversely
the datum descends to one pointed neighbourhood by finite presentation.
Thus the stalk colimit and strict-local cohomology agree in every degree.

The upper square commutes because both routes apply to a representative
$s\in I^r(\mathbf P^1_A\times_SV)$ by pulling it to
$\mathbf P^1_B\times_T(V\times_ST)$ and then to the pointed limit. This is
exactly the unit–counit formula defining the S0 exchange map. The lower
square commutes because restriction of that same section through $B$ and
then $k_B$ equals restriction through $k_A\cong k_B$; this also proves the
compatibility with differentials of $I^\bullet$.

The maps $\rho_A$ and $\rho_B$ are quasi-isomorphisms by Proposition
[prop-weil-pbc-p1-strict-henselian-comparison], and the bottom map is the
identity under $k_A\cong k_B$. Hence the top exchange stalk is an
isomorphism. Notice that no assertion is made here for a nontrivial
extension of separably closed residue fields; that is precisely the S5.2
curve-invariance input.
