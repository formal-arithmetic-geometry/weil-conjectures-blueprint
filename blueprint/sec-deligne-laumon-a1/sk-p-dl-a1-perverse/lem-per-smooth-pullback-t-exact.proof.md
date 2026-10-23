+++
kind  = "proof"
of    = "lem-per-smooth-pullback-t-exact"
+++
For the $\le$-direction: $Lf^*$ is exact (the cohomology sheaves
of $Lf^*K$ are the pullbacks of those of $K$) and the geometric
fibers of $f$ have dimension $d$, so the support of
$\mathcal H^{-i}(Lf^*K[d])$ has dimension at most the dimension of
the support of $\mathcal H^{-i+d}(K)$ plus $d$ (the pullback of a
constructible sheaf has support the preimage, of dimension raised by
the fibre dimension $d$, and the shift of the cohomology index is
$H^n(C[d])=H^{n+d}(C)$); hence

$$
\dim\operatorname{Supp}\mathcal H^{-i}\bigl(Lf^*K[d]\bigr)
\le\dim\operatorname{Supp}\mathcal H^{-i+d}(K)+d,
$$

and the support inequality for $K$ (applied to the index
$i-d$) gives
$\dim\operatorname{Supp}\mathcal H^{-i+d}(K)\le i-d$, so the
right-hand side is $\le i$, which is the support inequality
for $Lf^*K[d]$: $\operatorname{SuppCon}(Lf^*K[d])$.
For the $\ge$-direction: the cosupport condition of $K$, namely
$\operatorname{SuppCon}(D_YK)$, is transported along the smooth
morphism as follows. First, $D_XLf^*M\cong Rf^!D_YM$ for every $M$,
without any biduality: for a test complex $N$ on $X$, the adjunction
$Rf_!\dashv Rf^!$ of [fix-prop-adjunctions], the tensor–internal-Hom
adjunction of [def-weil-derived-pullback-tensor-hom] and the projection
formula of [fix-prop-projection-formula] give

$$
\begin{aligned}
\operatorname{Hom}_X(N,Rf^!D_YM)
&\cong\operatorname{Hom}_Y(Rf_!N\otimes^LM,\omega_Y)
\cong\operatorname{Hom}_Y\bigl(Rf_!(N\otimes^LLf^*M),\omega_Y\bigr)\\
&\cong\operatorname{Hom}_X(N\otimes^LLf^*M,Rf^!\omega_Y),
\end{aligned}
$$

naturally in $N$, so $Rf^!R\mathcal Hom_Y(M,\omega_Y)\cong
R\mathcal Hom_X(Lf^*M,Rf^!\omega_Y)$, and $Rf^!\omega_Y\cong\omega_X$ is the
mate of the composition isomorphism $R(a_Y f)_!\cong Ra_{Y!}Rf_!$ of
[thm-sf-comp-composition]. Combining this with the smooth
identity $Rf^!M\cong Lf^*M(d)[2d]$ (the smooth-purity form of the
dualizing complexes of the smooth morphism,
[cor-pur-adic-and-rational-smooth-dualizing-complexes] and [prop-functor-package]),

$$
D_X\bigl(Lf^*[d]K\bigr)
\cong Lf^*\bigl(D_YK\bigr)(d)[d].
$$

The twist $(d)$ is lisse of rank one, hence support-preserving
([lem-per-lisse-tensor-permanence]); the shift by $[d]$ moves
the cohomology index by $d$, i.e. $H^{-i}(Lf^*(D_YK)(d)[d])=H^{-i+d}(Lf^*(D_YK)(d))$, with the same
dimension bookkeeping as in the $\le$-direction; the support
inequality for $D_YK$ therefore implies the one for
$Lf^*D_YK(d)[d]$, i.e. $\operatorname{SuppCon}\bigl(D_X(Lf^*[d]K)\bigr)$, and the
$\ge$-inclusion follows from [def-per-support-condition].
