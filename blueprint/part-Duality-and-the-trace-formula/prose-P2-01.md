+++
id = "prose-P2-01"
kind = "hidden"
title = "Duality and the trace formula"
order = 721
+++
At the end of Part I we have, for every separated
$X_0$ of finite type over $\mathbf F_q$, cohomology groups $H^i_c$ with an
action of Frobenius, and they are finite because $Rf_!$ preserves $D^b_{\mathrm{ctf}}$.
Nothing yet connects them with the numbers $\#X_0(\mathbf F_{q^m})$ of which
the zeta function is made. This part supplies the connection: Weil's axioms
(b) and (c), the trace formula and Poincaré duality, and with them
rationality and the functional equation (Section [sec-Rationality-and-the-functional-equation]).

For the elliptic curve $y^2=x^3-x$ over $\mathbf F_3$ these two axioms,
together with the single count $N_1=4$, determine the zeta function and
every $N_m$ (Chapter [chap-The-trace-formula],
Example [example-running-example-trace-formula]).

Both axioms are statements about the diagonal. For example, on a compact
oriented manifold $M$, the Künneth components of the class of the diagonal
in $H^*(M\times M)$ form the copairing inverse to the cup product pairing,
and the Lefschetz number of a map $\varphi$ is the intersection number of
its graph with the diagonal. A scheme, however, comes with no orientation
and no class of the diagonal, and smooth purity is what provides them. It
says that
$f^!\simeq f^*(d)[2d]$ for $f$ smooth of relative dimension $d$
(Theorem [theorem-smooth-purity-all-admissible-coefficients]), and this
isomorphism gives the trace map.

Verdier duality (Theorems [theorem-verdier-biduality]
and [theorem-global-verdier-duality]) says that $\mathbb D=\cHom(-,\omega)$
is an involution of $D^b_{\mathrm{ctf}}$ exchanging $Rf_!$ with $Rf_*$. For smooth proper
$X$ it turns the trace map into a perfect pairing between $H^i$ and
$H^{2d-i}(d)$ (Corollary [corollary-cup-product-pairing]), and this
pairing is compatible with Frobenius
(Theorem [theorem-poincare-duality-frobenius]). Verdier duality also
gives the vanishing in (a) for such $X$
(Theorem [theorem-trace-isomorphism-top-degree]).

For the trace formula we use the Künneth formula for Verdier duals
(Lemma [lemma-external-duality-trace-morphism]), which turns a
correspondence $u:c_2^*K\to c_1^!K$ into a class on $C$; for an
endomorphism, $C$ is the graph. Restricting this class to the diagonal
gives the Lefschetz–Verdier formula
(Theorem [theorem-proper-pushforward-lefschetz-verdier]), which says that
on a proper scheme the trace of $u$ on cohomology is a sum of local terms
over the fixed locus.

This does not yet count points, for two reasons. A local term is computed
from $\cHom(c_2^*K,c_1^!K)$ near a fixed point, and the stalk of $K$ does
not determine it (Remark [remark-locality-warning]). Moreover $X$ need
not be proper. Both problems are settled by one computation on a curve: the
local term of Frobenius at a rational point is the trace on the stalk
(Proposition [proposition-frobenius-local-term-curve]). The computation
works because Frobenius has zero differential, so that its graph meets
the diagonal with multiplicity one and is tangent to a coordinate axis. The
result is the Grothendieck–Lefschetz trace formula
(Theorem [theorem-grothendieck-lefschetz-trace-formula]): for every Weil
complex $K$, $\operatorname{tr}(\operatorname{Frob}^m\mid R\Gamma_c(X,K))$ is the
sum over $X_0(\mathbf F_{q^m})$ of the traces of Frobenius on the stalks.

Smooth purity and Verdier duality hold over any finite or algebraically
closed field, and their compatibility with Frobenius follows from their
construction (Section [sec-Weil-complexes]).
