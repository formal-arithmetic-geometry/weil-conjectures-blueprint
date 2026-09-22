+++
id = "thm-sc-serre-duality-curve"
kind = "theorem"
title = "Serre duality for smooth proper curves"
order = 3658
lean = ["AlgebraicGeometry.Curve.serreDuality"]
uses = ["def-sc-kahler-differentials", "lem-sc-canonical-sheaf", "lem-sc-deg-principal-zero", "lem-sc-smooth-regular", "lem-sc-morphism-from-function", "thm-sc-p1-duality", "lem-sc-finite-duality"]
+++
Let $k$ be an algebraically closed field, $C$ a proper smooth curve over
$k$ and $\mathcal M$ an invertible $\mathcal O_C$-module. Then
$H^1(C,\mathcal M)$ and
$H^0(C,\Omega^1_{C/k}\otimes\mathcal M^{-1})$ are finite-dimensional
$k$-vector spaces (coherent cohomology of a proper scheme over a field is
finite-dimensional: *Source: Stacks Project, Cohomology of Schemes,
Proposition 30.19.1, [Tag 02O5](https://stacks.math.columbia.edu/tag/02O5)*),
and there is a canonical isomorphism
$$
 H^1(C,\mathcal M)^{\vee}\;\cong\;
 H^0\bigl(C,\;\Omega^1_{C/k}\otimes\mathcal M^{-1}\bigr),
$$
where $\Omega^1_{C/k}$ is the sheaf of Kähler differentials of $C$ over $k$
[def-sc-kahler-differentials].

## Proof

Put $\omega_C:=\Omega^1_{C/k}$, a line bundle [lem-sc-canonical-sheaf]; by
[def-sc-kahler-differentials] the sheaf $\omega_C\otimes\mathcal M^{-1}$ is
quasi-coherent.

*Case $\dim C=0$.* The finite-type scheme $C$ has finitely many points (it
is Noetherian of dimension zero), so the morphism
$C\to\operatorname{Spec}k$ is proper with finite fibres, hence finite by the
finite-iff-proper-with-finite-fibres theorem of the quasi-finite chapter;
thus $H^0(C,\mathcal O_C)$ is a finite-dimensional $k$-algebra, reduced
because $C$ is smooth, and connected because $C$ is connected, hence equal
to $k$ (a reduced finite-dimensional algebra over the algebraically closed
field $k$ is a product of finitely many copies of $k$, and connectedness
leaves one factor). So $C=\operatorname{Spec}k$: then
$H^1(C,\mathcal M)=0$ by affine vanishing ($\operatorname{Spec}k$ is
affine, $\mathcal M$ quasi-coherent), and $\Omega^1_{C/k}=0$: the module of
Kähler differentials of $k$ over $k$ with its universal derivation is zero
(the universal derivation of the identity is $d=0$), so
$H^0(C,\Omega^1_{C/k}\otimes\mathcal M^{-1})=0$: the claim.

*Case $\dim C=1$.* The connected smooth curve $C$ is integral: its local
rings are domains [lem-sc-smooth-regular], so its irreducible components
are pairwise disjoint (a point belonging to two components would have a
local ring with two minimal primes), and connectedness leaves a single
component. The function field $k(C)$ has transcendence degree one over $k$:
for an integral scheme of finite type over a field,
$\dim X=\operatorname{trdeg}_k k(X)$, by Noether normalization (*Source:
Stacks Project, Commutative Algebra, [Tag
00OY](https://stacks.math.columbia.edu/tag/00OY)*; as in the proof of
[lem-sc-deg-principal-zero]). Choose $t\in k(C)\setminus k$ (a
transcendental element, since $k\subset k(C)$ is a field extension and $k$
is algebraically closed), and let $f:=\pi_t:C\to\mathbf P^1_k$ be the
morphism of [lem-sc-morphism-from-function]: finite, surjective and flat,
of degree $d:=[k(C):k(t)]$.

*Transfer of the cohomology.* The morphism $f$ is proper (finite morphisms
of schemes are proper, by the finite-implies-proper lemma of the
ambient-foundations chapter), and its fibres are finite (finite implies
quasi-finite, and quasi-finite implies finite fibres, both in the
quasi-finite chapter); $\mathbf P^1_k$ is locally Noetherian (of finite
type over the field $k$). The line bundle $\mathcal M$ is coherent (on the
locally Noetherian scheme $C$, a locally free module of finite type is
coherent), so the formal-functions vanishing gives
$(R^p f_*\mathcal M)_y=0$ for all $p>0$ and all $y\in\mathbf P^1_k$, i.e.
$R^1f_*\mathcal M=0$ (a sheaf with vanishing stalks is zero), and the
low-degree terms of the Leray spectral sequence give
$$
 H^1(C,\mathcal M)\cong H^1(\mathbf P^1_k,f_*\mathcal M).
$$
Moreover $f_*\mathcal M$ is a finite locally free
$\mathcal O_{\mathbf P^1_k}$-module (of rank $d$): over an affine open
$U=\operatorname{Spec}R\subset\mathbf P^1_k$ the preimage
$f^{-1}(U)=\operatorname{Spec}B$ is affine with $B$ a finite locally free
$R$-algebra (finite flat), and $f_*\mathcal M|_U$ is the finite locally
free $R$-module $\Gamma(f^{-1}(U),\mathcal M)$, the sections of a line
bundle on the affine scheme $\operatorname{Spec}B$ over the finite
$R$-algebra $B$; its generic rank is $d=\dim_{k(t)}k(C)$.

*Duality.* Since $f_*\mathcal M$ is finite locally free, hence coherent,
[thm-sc-p1-duality] gives
$$
 H^1(\mathbf P^1_k,f_*\mathcal M)^{\vee}
 \cong
 \operatorname{Hom}_{\mathcal O_{\mathbf P^1}}
 \bigl(f_*\mathcal M,\omega_{\mathbf P^1}\bigr),
$$
and since $f$ is finite flat, [lem-sc-finite-duality] gives
$$
 \operatorname{Hom}_{\mathcal O_{\mathbf P^1}}
 \bigl(f_*\mathcal M,\omega_{\mathbf P^1}\bigr)
 \cong
 H^0\bigl(C,\omega_C\otimes\mathcal M^{-1}\bigr).
$$
Composing (the three isomorphisms are compatible with the identification
$\omega_C=\Omega^1_{C/k}$):
$$
 H^1(C,\mathcal M)^{\vee}
 \cong H^1(\mathbf P^1_k,f_*\mathcal M)^{\vee}
 \cong \operatorname{Hom}_{\mathcal O_{\mathbf P^1}}
 \bigl(f_*\mathcal M,\omega_{\mathbf P^1}\bigr)
 \cong H^0\bigl(C,\Omega^1_{C/k}\otimes\mathcal M^{-1}\bigr),
$$
which is the claim.

Unresolved dependencies: def:sc-curves, def:sc-invertible-module, def:sc-function-field, thm:pqf-finite-iff-proper-finite-fibres, pqf-lem-affine-vanishing, lem:weil-pbc-finite-proper, pqf-lem-finite-qf, pqf-lem-qf-finitefibres, pqf-def-coherent, pqf-lem-fff-vanishing, pqf-lem-sheaf-zero-stalks, pqf-lem-leray-lowdegree
