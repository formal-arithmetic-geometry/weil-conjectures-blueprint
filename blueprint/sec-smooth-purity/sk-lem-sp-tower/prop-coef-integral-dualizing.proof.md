+++
kind  = "proof"
of    = "prop-coef-integral-dualizing"
+++
By [sk-thm-existence], (3) and (4), $Ra^!_R$ exists and sends
$D^b_c(\operatorname{Spec}k,R)$ into $D^b_c(X,R)$, so $\omega_{X,R}\in D^b_c(X,R)$.
The coefficient comparison for the exceptional inverse image along
$R\to A_n$ is an isomorphism $\omega_{X,R}\otimes^{\mathbf L}_RA_n\cong\omega_{X,n}$
([sk-prop-scalar-six]), compatible with the reductions $A_n\to A_m$ and with the
comparisons of [lem-coef-finite-dualizing]. Objects of $D^b_c(X,R)$ are
derived complete ([sk-prop-integral-criterion]), so
$\omega_{X,R}\cong R\varprojlim_n\omega_{X,R}\otimes^{\mathbf L}_RA_n
\cong R\varprojlim_n\omega_{X,n}$. The Tor interval is read off on the
reductions. The finite preservation bound of
[lem-weil-verdier-preservation-strata], transported by
[lem-weil-finite-duality-site-comparison], gives $[-2d,0]$ for $\omega_{X,n}$,
by taking the constant input.

For the adjunction, the map

$$
R\operatorname{Hom}_X(K,\omega_{X,R})\xrightarrow{Ra_!}
R\operatorname{Hom}(Ra_!K,Ra_!\omega_{X,R})\xrightarrow{\varepsilon}
R\operatorname{Hom}_R(Ra_!K,R)
$$

induces on $H^i$ the adjunction bijection
$\operatorname{Hom}(K,\omega_{X,R}[i])\cong\operatorname{Hom}(Ra_!K,R[i])$ of
$Ra_!\dashv Ra^!_R$, so it is an isomorphism. As a consequence, it agrees with
the limit of the finite adjunctions. The finite exceptional adjoints of
[thm-sf-ambient-adjoint-class] and the compact-support reduction
[lem-coef-integral-compact-support] give, by derived extension and restriction of
scalars,

$$
\begin{aligned}
R\operatorname{Hom}_X(K,\omega_{X,R})
&\cong R\varprojlim_n R\operatorname{Hom}_{X,A_n}(K_n,\omega_{X,n})\\
&\cong R\varprojlim_n R\operatorname{Hom}_{A_n}(Ra_{!,n}K_n,A_n)
\cong R\operatorname{Hom}_R(Ra_!K,R).
\end{aligned}
$$

Here the middle isomorphism is the finite adjunction on derived mapping
complexes: it is [prop-asd-internal-adjunction] on the étale site, transported by
the finite site comparisons. The counits are compatible with reduction
([sk-prop-scalar-six]), so the two descriptions agree.
