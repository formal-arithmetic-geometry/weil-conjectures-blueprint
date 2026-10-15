+++
kind  = "proof"
of    = "prop-coef-integral-exceptional-adjoint"
+++
By [lem-coef-finite-exceptional] the displayed exceptional
tower is normalized, including its adjunction maps. Alternatively,
consider the integral object
$H=D_{X,R}f^*_{\mathrm{comp}}D_{Y,R}L$.
It exists in the integral category by
[thm-coef-integral-verdier] and
[lemma-weil-pbc-completed-pullback-reduction].
The latter gives finite reductions equal to ordinary pullback;
pullback preserves the reduction Tor interval. Applying the two
duality bounds gives $[a-2\dim X,b+2\dim Y]$.
The finite dual formula in [lem-coef-finite-exceptional]
identifies its reductions with $Rf_n^!L_n$, compatibly with
the transition maps. Reconstruction, or
[lem-coef-normalized-dvr-effectivity], gives $H\cong G_fL$.

For $K\in D^b_c(X,R)$, use the reduction of integral compact
supports in [lem-coef-integral-compact-support] and derived
coefficient adjunction to compute

$$
\begin{aligned}
R\operatorname{Hom}_Y(Rf_!K,L)
&\cong R\varprojlim_n R\operatorname{Hom}_{Y,A_n}(Rf_{!,n}K_n,L_n)\\
&\cong R\varprojlim_n R\operatorname{Hom}_{X,A_n}(K_n,Rf_n^!L_n)\\
&\cong R\operatorname{Hom}_X(K,G_fL).
\end{aligned}
$$

Finite units and counits commute with the transition maps by
[lem-coef-finite-exceptional]. Hence this calculation defines
the adjunction and its specified maps; the triangle identities
follow from the same identities before taking the derived limit.
For the structure morphism and $L=R$, the defining tower is
the one in [prop-coef-integral-dualizing]. This proves the
last identification with its adjunction, without an assertion about
unrestricted unbounded pro-etale inputs.
