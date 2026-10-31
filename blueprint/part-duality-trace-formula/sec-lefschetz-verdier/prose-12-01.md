+++
id = "prose-12-01"
kind = "hidden"
title = "Weil complexes and the Lefschetz–Verdier formula"
order = 528
+++
For a self-map $\varphi$ of a compact oriented manifold $M$, the
Lefschetz number is the intersection number of the graph with the
diagonal (Part “Duality and the trace formula”), and the fixed locus need not be
discrete. For $\varphi=\operatorname{id}$ it is all of $M$, and the
formula becomes $\chi(M)=\int_Me(TM)$, the self-intersection of the
diagonal. In general the global side is a trace on cohomology, and the
local side is a sum of contributions, one for each connected component
of the fixed locus, each computed in a neighbourhood of that component.
To prove such a formula for Frobenius we need the global side to be
defined, and we need a definition of the local contributions that works
for constructible coefficients and arbitrary fixed loci.

The first need is met by Weil structures. Over $k=\overline{\mathbf F}_q$
an arbitrary scheme has no Frobenius endomorphism acting on its
cohomology; a model $X_0$ over $\mathbf F_q$ provides one. It endows
$X=X_0\times_{\mathbf F_q}k$ with the geometric Frobenius
$\operatorname{Fr}_X$. A complex $K$ pulled back from $X_0$ comes with an
isomorphism $\phi_K:\operatorname{Fr}_X^*K\simeq K$; such an isomorphism
is a Weil structure (Definition [sk-def-sf-weil-complexes]). A Weil structure induces the
Frobenius operator $\operatorname{Frob}_{X,K}$ on $R\Gamma_c(X,K)$ and on
every stalk at a fixed point, and these are the two sides of the trace
formula. Smooth purity, the trace map and Poincaré duality respect
Weil structures, with the twist $\Lambda(-1)$ on which geometric
Frobenius acts by $q$ (Proposition [sk-prop-prop-sp-frobenius-purity] and
Theorem [sk-thm-frobenius]). This is the form of duality behind the
relation $\alpha\leftrightarrow q^d/\alpha$ of Weil's axiom (c).

The second need is met by Grothendieck's formalism of cohomological
correspondences, written up by Illusie in (SGA5, III). A correspondence on $X$ is a map
$c=(c_1,c_2):C\to X\times X$, and a cohomological correspondence on $K$
is a morphism $u:c_2^*K\to c_1^!K$. For the graph of an endomorphism
$\varphi$ this is just a map $\varphi^*K\to K$, and for Frobenius it is
$\phi_K$, up to the comparison of $\operatorname{Fr}_X$ with the
$k$-linear Frobenius in Section [sec-trace-formula]. When $c_2$ is
proper, $u$ induces an endomorphism $T_c(u)$ of $R\Gamma_c(X,K)$. The local
contribution comes from duality. The Künneth formula for Verdier duals
identifies $\cHom(c_2^*K,c_1^!K)$ with $c^!(K\boxtimes\mathbb D_XK)$
(Lemma [sk-thm-sf-kunneth-verdier]). Thus $u$ is a class on $C$, and
pairing it on the diagonal by evaluation
$K\otimes^{\mathbf L}\mathbb D_XK\to\omega_X$ gives the trace class
$\operatorname{Tr}_c(u)\in H^0(\Fix(c),\omega_{\Fix(c)})$, supported on the
fixed locus. Its integral over a proper open and closed part $B$ of
$\Fix(c)$ is the local term $\operatorname{LT}_B(u)$. The
Lefschetz–Verdier formula (Theorem [sk-p-proper]) says
that if $X$ and $C$ are proper over $k$, then

$$
\operatorname{tr}\bigl(T_c(u)\mid R\Gamma(X,K)\bigr)
=\sum_B\operatorname{LT}_B(u).
$$

Its proof is a compatibility rather than a computation: trace classes
commute with proper pushforward of correspondences, and pushing forward
to the identity correspondence of the point turns the trace class into
the trace of $T_c(u)$ on the perfect complex $R\Gamma(X,K)$
(Lemma [sk-p-pairing]). The formula is a statement in
$A$, without any condition on the fixed locus. It does not compute the
individual local terms. Computing them for
Frobenius is the subject of Section [sec-trace-formula].

With coefficients in a finite ring $A$, both sides are traces
of endomorphisms of perfect complexes (Definition [sk-d-trace]),
not alternating sums of traces on cohomology modules, which need not be
projective. The trace is not even determined by the maps induced on
cohomology. On $P=[\mathbf Z/\ell^2\xrightarrow{\ell}\mathbf Z/\ell^2]$
the chain maps $(1,1)$ and $(1+\ell,1)$ both induce the identity on
$H^0(P)$ and $H^1(P)$, but their traces are $0$ and $\ell$
(Example [sk-ex-tf-trace-example]). Since cones are not functorial,
additivity of traces in a distinguished triangle can fail. It holds for
endomorphisms of a triangle in the filtered derived category
[Stacks, Tag 087J](https://stacks.math.columbia.edu/tag/087J) (Remark [sk-rem-tf-coherent-additivity]), and additivity of trace classes
along an invariant open subscheme and its complement is proved in this
form (Proposition [sk-i-additivity]). Finite rings such as
$\mathcal O_E/\pi_E^n$ cannot be avoided, since the trace formula over
$\mathcal O_E$ is obtained from its reductions.

Throughout, $k_0=\mathbf F_q$, $k=\overline{\mathbf F}_q$ and
$s=\operatorname{Spec}k$. For a scheme $X$ over $k$, $a_X:X\to s$
is the structure morphism, and $X=X_0\times_{k_0}k$ whenever a model
$X_0$ over $k_0$ is given. In Section [sec-frobenius] the coefficient ring
$\Lambda$ is any admissible ring; from Section [sec-tf-categorical-trace]
until Section [sec-tf-coefficient-transport] it is an arbitrary finite commutative
$\ell$-primary ring $A$, with $\ell\ne\operatorname{char}k$. We write $\omega_X=a_X^!A_s$ and
$\mathbb D_XK=\cHom_A(K,\omega_X)$ for the dualizing complex and the
Verdier dual of Definition [sk-def-ops] with coefficients $A$.
In some proofs we compute on small
étale sites and transport the result by means of the comparison
theorems for complexes of finite Tor amplitude.
