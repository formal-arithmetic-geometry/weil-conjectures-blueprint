+++
kind = "proof"
of = "det-ctf-finite-compact-proetale"
+++
By [sk-prop-pe-unbounded-classical], $\nu_X^*\colon\D(X_{\mathrm{ét}},A)\to\D(X_{\mathrm{proét}},A)$ is exact, fully
faithful and preserves arbitrary direct sums; by [sk-cor-pe-finite-tor-comparison] it restricts to an
equivalence $\Dctf(X_{\mathrm{ét}},A)\simeq\Dctf(X,A)$.

The essential image $\mathcal I$ of $\nu_X^*$ is a triangulated subcategory closed under sums (by exactness,
full faithfulness and sum preservation), containing $\Dctf(X,A)$; hence $\Loc(\Dctf(X,A))\subset\mathcal I$
([sk-def-localizing-closure]). Thus every $K_s\in\Loc(\Dctf(X,A))$ is $\nu_X^*K_s^{\mathrm{ét}}$, and
$C=\nu_X^*C^{\mathrm{ét}}$ with $C^{\mathrm{ét}}\in\Dctf(X_{\mathrm{ét}},A)$. Then

$$
\Hom\Bigl(C,\bigoplus K_s\Bigr)=\Hom\Bigl(\nu_X^*C^{\mathrm{ét}},\nu_X^*\bigoplus K^{\mathrm{ét}}_s\Bigr)
=\Hom\Bigl(C^{\mathrm{ét}},\bigoplus K^{\mathrm{ét}}_s\Bigr)=\bigoplus\Hom(C^{\mathrm{ét}},K^{\mathrm{ét}}_s)=\bigoplus\Hom(C,K_s),
$$

using sum preservation, full faithfulness and [det-ctf-finite-compact-etale]. Sums in $\Loc(\Dctf(X,A))$ are
the ambient ones, so $C$ is compact there.
