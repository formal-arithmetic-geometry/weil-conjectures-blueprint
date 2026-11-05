+++
id = "prose-11-01"
kind = "hidden"
title = "The Lefschetz–Verdier formula"
order = 891
+++
The trace formula has to express the trace of Frobenius on $R\Gamma_c(X,K)$ as a
sum over the fixed points of Frobenius, that is, over $X_0(\mathbf F_{q^m})$. We
do not prove it for Frobenius directly. Instead we first prove a fixed point
formula for every correspondence on a proper scheme. In this generality the
formula is compatible with proper pushforward, and pushing forward to a point
turns it into a tautology.

For a general correspondence, however, the fixed locus need not be discrete
(Section [sec-Trace-classes-and-local-terms]). The local side is then a sum of contributions, one for
each connected component of the fixed locus, each computed in a neighbourhood of
that component.

We use Grothendieck's formalism of cohomological correspondences, written up by
Illusie in [sga5, III]. In this formalism, a correspondence on $X$ is a map
$c=(c_1,c_2):C\to X\times X$, and a cohomological correspondence on $K$ is a
morphism $u:c_2^*K\to c_1^!K$. For example, for the graph of an endomorphism $\varphi$ this is a map $\varphi^*K\to K$. In particular, for Frobenius it is the Weil structure
$\phi_K:\operatorname{Fr}_X^*K\simeq K$ of Section [sec-Weil-complexes], up to the
comparison of $\operatorname{Fr}_X$ with the $k$-linear Frobenius in
Section [chap-The-trace-formula]. When $c_2$ is proper, $u$ induces an endomorphism
$T_c(u)$ of $R\Gamma_c(X,K)$. In the same way $\phi_K$ induces the Frobenius operator
$\operatorname{Frob}_{X,K}$ on $R\Gamma_c(X,K)$ and on every stalk at a fixed point.

The local contributions come from duality, as $\operatorname{Hom}(V,V)=V\otimes
V^\vee$ turns an endomorphism into a tensor whose evaluation is the trace. In this
way $u$ gives the trace class $\operatorname{Tr}_c(u)\in H^0(\Fix(c),\omega_{\Fix(c)})$,
supported on the fixed locus. Its integral over a proper open and closed part $B$ of
$\Fix(c)$ is the local term $\operatorname{LT}_B(u)$. The Lefschetz–Verdier formula
(Theorem [theorem-proper-pushforward-lefschetz-verdier]) says that if $X$ and $C$
are proper over $k$, then

$$
\operatorname{tr}\bigl(T_c(u)\mid R\Gamma(X,K)\bigr)
=\sum_B\operatorname{LT}_B(u).
$$

The proof involves no computation, because trace classes commute with proper pushforward of correspondences. After pushing forward to the identity correspondence of the point,
the trace class becomes the trace of $T_c(u)$ on the perfect complex $R\Gamma(X,K)$
(Lemma [lemma-local-terms-point]). The price of this generality, however, is that the formula does not compute the individual local terms; for Frobenius that is done in
Section [chap-The-trace-formula].

With coefficients in a finite ring $A$ both sides are traces of endomorphisms of
perfect complexes (Definition [definition-categorical-trace]). They are not
alternating sums of traces on cohomology modules, since these need not be
projective. In fact, the trace is not even determined by the maps induced on cohomology
(Example [example-trace-not-determined-cohomology]). Moreover, finite rings such as $\mathcal O_E/\pi_E^n$ cannot be avoided, because the trace formula over
$\mathcal O_E$ is obtained from its reductions.

Throughout, $k_0=\mathbf F_q$, $k=\overline{\mathbf F}_q$ and
$s=\operatorname{Spec}k$. For a scheme $X$ over $k$, $a_X:X\to s$
is the structure morphism, and $X=X_0\times_{k_0}k$ whenever a model
$X_0$ over $k_0$ is given. From Section [sec-Traces-of-perfect-complexes] until Section [sec-ell-adic-coefficients-5] the coefficient ring is an arbitrary finite commutative
$\ell$-primary ring $A$, with $\ell\ne\operatorname{char}k$, and we write $\omega_X=a_X^!A_s$ and
$\mathbb D_XK=\cHom_A(K,\omega_X)$ for the dualizing complex and the
Verdier dual of Definition [definition-verdier-dual-evaluation] with coefficients $A$.
Some proofs compute on small
étale sites and transport the result by means of the comparison
theorems for complexes of finite Tor amplitude.
