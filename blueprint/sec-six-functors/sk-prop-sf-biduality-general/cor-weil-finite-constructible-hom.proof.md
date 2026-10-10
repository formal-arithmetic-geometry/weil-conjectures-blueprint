+++
kind  = "proof"
of    = "cor-weil-finite-constructible-hom"
+++
The tensor–Hom adjunction of
[def-weil-derived-pullback-tensor-hom] and biduality
[thm-fix-general-biduality] give the natural identity

$$
R\mathcal Hom_A(K,L)
\cong R\mathcal Hom_A(K,D_XD_XL)
\cong D_X(K\otimes_A^LD_XL).
$$

By [lem-weil-verdier-preservation-strata], $D_XL$ has Tor
interval $[-e-2d,-c]$. Tensor preservation
[lem-sf-tensor-ctf] gives interval $[a-e-2d,b-c]$ for the
tensor inside the last dual. Apply the same duality bound again to
obtain $[c-b-2d,e-a+2d]$. All the objects are constructible by
the same two results. The argument on the pro-etale site is the
transport by [lem-weil-finite-duality-site-comparison]; it makes
no site-perfectness assumption on $K$ or $L$ on all of $X$.
