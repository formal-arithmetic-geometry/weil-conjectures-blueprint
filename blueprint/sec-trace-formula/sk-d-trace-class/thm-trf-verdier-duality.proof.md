+++
kind  = "proof"
of    = "thm-trf-verdier-duality"
+++
Step 1 (the first comparison). Apply the Kunneth–Verdier isomorphism
[thm-trf-kunneth-verdier] of the trace-formula chapter to the case
$X=Y$, $M=N=K$. With the projections $p_1,p_2:X\times_sX\to X$,
its source $M\boxtimes_A^{\mathrm L}D_YN$ becomes
$K\boxtimes_A^{\mathrm L}D_XK$ and its target
$\RHom_A(p_Y^*N,p_X^!M)$ becomes
$\RHom_A(p_2^*K,p_1^!K)$, so

$$
\kappa_{K,K}:K\boxtimes_A^{\mathrm L}D_XK
\xrightarrow{\ \sim\ }
\RHom_A(p_2^*K,p_1^!K)
$$

is the first display, read in the inverse direction.

Step 2 (the second comparison). By [def-trf-trace-class-source],

$$
\mathcal H_c(K)=R\mathcal Hom_A\bigl(Lc_2^*K,Rc_1^!K\bigr) .
$$

Since $Lc_2^*=c^*p_2^*$ and $Rc_1^!=(p_1c)^!=c^!p_1^!$ by the
composition identities of the six-operation package, the exceptional
internal-Hom exchange [lem-trf-exceptional-internal-hom-exchange],
applied to the admissible $c$ with $M=p_2^*K$ and $N=p_1^!K$, gives

$$
R\mathcal Hom_A\bigl(c^*p_2^*K,c^!p_1^!K\bigr)
\cong
c^!R\mathcal Hom_A(p_2^*K,p_1^!K).
$$

Composing with the inverse of Step 1 under $c^!$ yields the second
display.

Step 3 (compatibilities). The isomorphism of Step 1 is $\kappa_{K,K}$,
which by its construction in [thm-trf-kunneth-verdier] is the
adjoint-canonical comparison, hence compatible with evaluation and with
the tensor–Hom adjunction; the exchange of Step 2 is likewise
adjoint-canonical by [def-trf-admissibility]. Both compatibilities
therefore hold.
