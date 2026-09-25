+++
id = "sk-prop-stalk"
kind = "section"
title = "P3: the stalks are fibre integrals"
order = 2894
uses = ["sk-def-ft", "sk-def-kernel"]
+++
*Proposition (sketch).*

Let $S=\Spec k$, $V\cong\mathbf A^r_k$, let $\bar\xi$ be a geometric point of
$V^\vee$ and $K\in\Dbc(V,E)$. Then

$$
\bigl(\FT_\psi(K)\bigr)_{\bar\xi}
\cong H^*_c\bigl(V_{\bar k},\,K\otimes^L\mathcal L_{\psi(\langle x,\xi\rangle)}\bigr)[r].
$$

(Blueprint lem:fd-stalk-formula.)

## Proof

The strict-henselization stalk formula
prop:weil-pbc-strict-henselization-stalk-formula for the
compact-support direct image identifies the stalk at $\bar\xi$ with the
compactly supported cohomology of the strict-local fibre
$V_{\bar k}\times_k\Spec\mathcal O^{\mathrm{sh}}_{V^\vee,\bar\xi}$. On that
fibre the kernel restricts to the pullback of
$K\otimes^L\mathcal L_{\psi(\langle x,\xi\rangle)}$: the pairing restricts to
$\langle x,\xi\rangle$, and since the Artin–Schreier sheaf is lisse its
inverse image is the sheaf of the restricted function. The structure
morphism of the strict-local fibre is a limit of étale morphisms, hence
smooth, so $\Qlb$-coefficient smooth base change
(sbc-thm-overline-mathbf-q-ell-coefficient-smooth-base-ch) identifies the
two compactly supported groups, the compactification step being
thm:weil-pbc-qbar.

Uses: [sk-def-ft], [sk-def-kernel]
