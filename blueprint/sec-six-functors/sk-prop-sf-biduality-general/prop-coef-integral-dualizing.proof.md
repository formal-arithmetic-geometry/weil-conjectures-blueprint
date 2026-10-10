+++
kind  = "proof"
of    = "prop-coef-integral-dualizing"
+++
The coherent comparisons of [lem-coef-finite-dualizing] make
$(\omega_{X,n})_n$ a normalized tower. Effectivity
[lem-coef-normalized-dvr-effectivity] gives the displayed
reductions and completeness. The finite preservation bound of
[lem-weil-verdier-preservation-strata], transported by
[lem-weil-finite-duality-site-comparison], gives
$[-2d,0]$ by taking the constant input. Thus all finiteness
conditions of the integral category are checked on these identified
reductions.

For the adjunction, use the finite exceptional adjoints of
[thm-sf-ambient-adjoint-class] on bounded constructible inputs
and the compact-support reduction
[lem-coef-integral-compact-support]. At finite level the
adjunction on derived mapping complexes follows by applying derived
global sections to [prop-asd-internal-adjunction] on the etale site
and transporting it by the already stated finite site comparisons.
Thus this is an adjunction of mapping complexes before taking limits.
Derived extension–restriction of scalars and preservation of limits in the
second mapping variable give

$$
\begin{aligned}
R\operatorname{Hom}_X(K,\omega_{X,R})
&\cong R\varprojlim_n R\operatorname{Hom}_{X,A_n}(K_n,\omega_{X,n})\\
&\cong R\varprojlim_n R\operatorname{Hom}_{A_n}(Ra_{!,n}K_n,A_n)\\
&\cong R\varprojlim_n R\operatorname{Hom}_R(Ra_!K,A_n)\\
&\cong R\operatorname{Hom}_R(Ra_!K,R).
\end{aligned}
$$

The last equality uses the complete coefficient object
$R=R\varprojlim A_n$. The transition maps in the second line
are those of the finite adjunctions: the dualizing comparisons are
defined by their counits. Hence all four lines identify the specified
natural maps. Taking degree zero gives the claimed adjunction,
without interchanging $H^0$ and an ordinary inverse limit.
