+++
kind  = "proof"
of    = "lem-coef-integral-hom-reduction"
+++
The complex $[R_X\xrightarrow{\pi^n}R_X]$ is a finite-free
resolution of $A_n$. Applying the exact $R$-linear functor
$R\mathcal Hom_R(K,-)$ to this two-term coefficient construction
gives

$$
R\mathcal Hom_R(K,L)\otimes_R^L A_n
\cong R\mathcal Hom_R(K,L\otimes_R^L A_n).
$$

The extension–restriction adjunction along $R_X\to A_n$
([sk-def-sfb-pulled-back-coefficients]) identifies the latter
with
$\operatorname{Res}_nR\mathcal Hom_{A_n}(K_n,L_n)$.
Indeed, testing on a complex on each slice of the site reduces this
identity to the derived tensor–Hom adjunction of
[sk-def-sfb-derived-tensor-hom]. The resulting map is
$A_n$-linear and is precisely the canonical comparison in the
statement. The finite-free construction and this adjunction use the
actual evaluation maps, which proves their compatibility as well.

If $L$ is complete, then $L\cong R\varprojlim_n\operatorname{Res}_nL_n$ by
[sk-def-pe-derived-completion].
Internal Hom preserves derived limits in its second variable, since
it is right adjoint to derived tensor. Consequently

$$
R\mathcal Hom_R(K,L)
\cong R\varprojlim_n\operatorname{Res}_n
R\mathcal Hom_{A_n}(K_n,L_n).
$$

The preceding comparison identifies this with
$R\varprojlim_n(R\mathcal Hom_R(K,L)\otimes^L_RA_n)$, so $R\mathcal Hom_R(K,L)$
is derived complete in the sense of [sk-def-pe-derived-completion].
This proof uses perfectness of $A_n$ over $R$, not
perfectness of $A_n$ over a larger finite quotient ring.
