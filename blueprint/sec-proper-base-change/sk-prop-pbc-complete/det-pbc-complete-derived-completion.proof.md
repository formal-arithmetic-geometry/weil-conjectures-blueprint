+++
kind = "proof"
of = "det-pbc-complete-derived-completion"
+++
Fix $m$ and put $R_m=[\mathcal O_{E,T}\xrightarrow{\pi_E^m}\mathcal O_{E,T}]$, so that
$\operatorname{red}(N)_m=N\otimes R_m$ ([det-pe-derived-nakayama-resolution]). By
[det-pbc-complete-tower-calculus] (5),

$$
\widehat M\otimes R_m\simeq R\varprojlim_n\bigl(M\otimes R_n\otimes R_m\bigr).
$$

For $n\geq m$ the complex $R_n\otimes R_m$ is quasi-isomorphic, compatibly with
the transitions in $n$, to $R_n\otimes(\mathcal O_E/\pi_E^m)_T=
[(\mathcal O_E/\pi_E^m)_T\xrightarrow{0}(\mathcal O_E/\pi_E^m)_T]$, which is the
direct sum of $(\mathcal O_E/\pi_E^m)_T$ in degree $0$, with identity
transitions, and $(\mathcal O_E/\pi_E^m)_T[1]$, with transitions multiplication
by $\pi_E$ (the degree $-1$ component of the transition maps of
[det-pbc-complete-towers] (3)). Hence the tower $(M\otimes R_n\otimes R_m)_{n\geq m}$
is the direct sum of the constant tower $c(M_m)$ and a tower $N_\bullet$ in
which every composite of $m$ transitions is multiplication by $\pi_E^m$, which
is zero on $M_m$. For $N_\bullet$ the endomorphism $T$ of $\prod_nN_n$ in the
Milnor cone satisfies $T^m=0$, so $1-T$ is invertible with inverse
$\sum_{k<m}T^k$, and $R\varprojlim N_\bullet=0$. Finitely many levels $n<m$ do
not change the derived limit. Therefore $\widehat M\otimes R_m\simeq
R\varprojlim c(M_m)\simeq M_m$, and this isomorphism is inverse to
$\kappa_M\otimes R_m$, since $\kappa_M\otimes R_m$ is induced by the inclusion of
the constant summand. The identifications are compatible with $m+1\to m$, which
gives the isomorphism of towers $\operatorname{red}(\kappa_M)$ (an isomorphism
in $D(\operatorname{Tow}(T))$ by [det-pbc-complete-tower-calculus] (2)).

Completeness of $\widehat M$. The same computation with the roles of $n$ and
$m$ exchanged shows that, for fixed $n$, the complex $N_n=M\otimes R_n$ is
derived complete: for $m\geq n$, $R_m\otimes R_n\simeq
[(\mathcal O_E/\pi_E^n)_T\xrightarrow{0}(\mathcal O_E/\pi_E^n)_T]$ compatibly with
the transitions in $m$, so $(N_n\otimes R_m)_m$ is the sum of the constant tower
$c(N_n)$ and a tower whose $n$-fold composites of transitions vanish, and
$\kappa_{N_n}\colon N_n\to R\varprojlim_m(N_n\otimes R_m)$ is an isomorphism. Now
$\widehat M=R\varprojlim_nN_n$, and by [det-pbc-complete-tower-calculus] (5)

$$
\widehat{\widehat M}=R\varprojlim_m\Bigl(\bigl(R\varprojlim_nN_n\bigr)\otimes R_m\Bigr)
\simeq R\varprojlim_mR\varprojlim_n(N_n\otimes R_m)
\simeq R\varprojlim_nR\varprojlim_m(N_n\otimes R_m),
$$

the last step because both iterated Milnor cones are the total complex of the
commutative square formed by $1-T_n$ and $1-T_m$ on
$\prod_{n,m}N_n\otimes R_m$. Under these identifications
$\kappa_{\widehat M}=R\varprojlim_n\kappa_{N_n}$, since both are induced by the
inclusions of the constant towers. Each $\kappa_{N_n}$ is an isomorphism, hence
so is $\kappa_{\widehat M}$, and $\widehat M$ is derived complete
([sk-def-pe-derived-completion]).
