+++
kind  = "proof"
of    = "lem-sfb-finite-upper-star-tensor"
uses = ["lem-sfb-finite-upper-star-exact", "lem-sfb-finite-upper-star-unit"]
+++
Write $a$ for sheafification and $\otimes_{\mathrm{pre}}$ for the objectwise tensor
product, so $F\otimes G=a(F\otimes_{\mathrm{pre}}G)$ ([lem-weil-pbc-sheaf-tensor-closed]). As in the
proof of [lem-sfb-finite-upper-star-unit], $g^*\circ a\cong a\circ\operatorname{Lan}_{b^{\mathrm{op}}}$.
The value of $\operatorname{Lan}_{b^{\mathrm{op}}}$ at $W$ is a filtered colimit (proof of
[lem-sfb-finite-upper-star-exact]). Since $\mathcal A$ is closed, $\otimes$ preserves
colimits in each variable, and a filtered colimit of a diagonal diagram $i\mapsto P_i\otimes Q_i$
is $\colim P_i\otimes\colim Q_i$. Hence
$\operatorname{Lan}_{b^{\mathrm{op}}}(P\otimes_{\mathrm{pre}}Q)\cong
\operatorname{Lan}_{b^{\mathrm{op}}}P\otimes_{\mathrm{pre}}\operatorname{Lan}_{b^{\mathrm{op}}}Q$.
Finally $a(P\otimes_{\mathrm{pre}}Q)\cong a(aP\otimes_{\mathrm{pre}}aQ)$, which is the
compatibility of sheafification with the tensor product from [lem-weil-pbc-sheaf-tensor-closed].
Together,

$$
g^*(F\otimes G)\cong a\bigl(\operatorname{Lan}F\otimes_{\mathrm{pre}}\operatorname{Lan}G\bigr)
\cong a\bigl(a\operatorname{Lan}F\otimes_{\mathrm{pre}}a\operatorname{Lan}G\bigr)
=g^*F\otimes g^*G,
$$

and the composite is the mate of the lax structure map. For $g$ weakly étale, $g^*$ is
restriction along the localization functor, and the statement is the compatibility of
sheafification with restriction along a continuous and cocontinuous functor.
