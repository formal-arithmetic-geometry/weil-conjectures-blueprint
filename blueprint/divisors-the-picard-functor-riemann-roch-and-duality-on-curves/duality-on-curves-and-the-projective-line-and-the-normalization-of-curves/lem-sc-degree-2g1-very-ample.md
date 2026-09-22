+++
id = "lem-sc-degree-2g1-very-ample"
kind = "lemma"
title = "Line bundles of large degree are very ample"
order = 3660
lean = ["AlgebraicGeometry.Curve.isVeryAmple_of_two_genus_add_one_le_degree"]
uses = ["def-sc-pic0", "lem-sc-negative-degree-no-sections", "lem-sc-riemann-roch", "lem-sc-canonical-degree", "thm-sc-serre-duality-curve"]
+++
Let $C$ be a proper smooth curve of genus $g$ over an algebraically closed
field $k$, and $\mathcal M$ a line bundle on $C$ with
$\deg\mathcal M\geq2g+1$ [def-sc-pic0]. Then $\mathcal M$ is very ample.

## Proof

We use the Riemann--Roch theorem for a proper smooth curve of genus $g$
[lem-sc-riemann-roch]: for a line bundle $\mathcal N$ of degree $d$,
$$
 \dim H^0(C,\mathcal N)-\dim H^1(C,\mathcal N)=d-g+1,
$$
and Serre duality
$H^1(C,\mathcal N)^{\vee}\cong H^0(C,\mathcal O_C(K_C)\otimes\mathcal N^{-1})$
[thm-sc-serre-duality-curve], with $\omega_C=\mathcal O_C(K_C)$ and
$\deg K_C=2g-2$ [lem-sc-canonical-degree]. The formula $\deg K_C=2g-2$ is
deduced from [lem-sc-riemann-roch] as follows: part (2) gives
$\deg(\omega_C)=-2\chi(C,\mathcal O_C)$, and
$\chi(C,\mathcal O_C)=1-g$ since $\dim H^0(C,\mathcal O_C)=1$ ($C$ is
proper and geometrically integral, so its global functions are the
constants $k$; by the definition of $\deg$ this also gives
$\chi(C,\mathcal O_C)=\deg\mathcal O_C-\tfrac12\deg\omega_C$, and
$\deg\mathcal O_C=0$) and $g=\dim H^1(C,\mathcal O_C)$.

First, $H^1(C,\mathcal M)=0$: the dual
$\mathcal O_C(K_C)\otimes\mathcal M^{-1}$ has degree $(2g-2)-d<0$, and a
line bundle of negative degree has no nonzero global sections
[lem-sc-negative-degree-no-sections]. Hence
$\dim H^0(C,\mathcal M)=d-g+1$. Similarly, for $P,Q\in C$ (possibly
equal), $\deg\mathcal M(-P-Q)=d-2\geq2g-1$, so
$H^1(C,\mathcal M(-P-Q))=0$ and
$$
 \dim H^0(C,\mathcal M(-P-Q))=\dim H^0(C,\mathcal M)-2,
$$
and $\deg\mathcal M(-P)=d-1\geq2g$, so
$\dim H^0(C,\mathcal M(-P))=\dim H^0(C,\mathcal M)-1$. These dimension
drops say exactly that the complete linear system $|\mathcal M|$ is base
point free and separates points and tangent vectors: the drop for
$\mathcal M(-P)$ gives a section not vanishing at $P$; the drop for
$\mathcal M(-P-Q)$ with $P\neq Q$ gives a section vanishing at $P$ but not
at $Q$ (and one vanishing at $Q$ but not at $P$); and with $P=Q$ it gives a
section vanishing at $P$ to order exactly one.

We now prove that these properties make the map
$\varphi:C\to\mathbf P^N$ associated to the complete linear system
$|\mathcal M|$ a closed immersion. A section vanishing at $P$ but not at
$Q$ shows $\varphi(P)\neq\varphi(Q)$. A section vanishing at $P$ to order
exactly one shows that $d\varphi_P$ is injective (a tangent direction at
$P$ is a first-order deformation of $P$, and such a section separates it
from the trivial deformation), and the injectivity of $d\varphi_P$ for all
$P$ is equivalent to $\Omega_{C/\mathbf P^N}=0$ (the fibre of
$\Omega_{C/\mathbf P^N}$ at $P$ is the dual of the cokernel of the tangent
map; *reference: Stacks Project, Morphisms of Schemes: unramified
morphisms*), i.e. $\varphi$ is unramified. An unramified morphism has
finite fibres (a scheme of finite type over a field with vanishing sheaf of
differentials is a finite disjoint union of points: its irreducible
components have function fields with no differentials, hence are algebraic
over the base field, so the dimension is zero and the finiteness of
zero-dimensional closed subsets applies). Thus $\varphi$ is proper (a
morphism of proper schemes) with finite fibres, hence finite (the
finite-iff-proper-with-finite-fibres theorem of the quasi-finite chapter;
*reference: Stacks Project, Cohomology of Schemes, [Tag
02OG](https://stacks.math.columbia.edu/tag/02OG): proper and quasi-finite
implies finite*). Finally, $\varphi$ is finite and injective on closed
points: its image $\varphi(C)\subset\mathbf P^N$ is closed, and for
$y=\varphi(P)\in\varphi(C)$ the fibre is the single point $P$ with residue
field $k$ ($k$ algebraically closed), so
$(\varphi_*\mathcal O_C)_y\otimes k(y)=k$; by Nakayama's lemma
$\mathcal O_{\mathbf P^N,y}\to(\varphi_*\mathcal O_C)_y$ is surjective,
hence an isomorphism (it is injective because $\varphi$ is dominant onto
$\varphi(C)$), and $\varphi$ is an isomorphism onto $\varphi(C)$, i.e. a
closed immersion. Hence $\mathcal M$ is very ample.

Unresolved dependencies: def:sc-genus, def:sc-curves, def:sc-ample, lem:sc-dim0-finite, thm:pqf-finite-iff-proper-finite-fibres
