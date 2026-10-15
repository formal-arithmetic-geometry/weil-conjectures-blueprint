+++
kind = "proof"
of = "sk-prop-sp-orientation"
uses = ["sk-prop-sp-exceptional-bc", "sk-thm-dnc", "sk-prop-an"]
+++
The projection $p_1$ is the base change of $f$ along $f$, so
[sk-prop-sp-exceptional-bc] gives $\omega_{p_1}\simeq p_2^{*}\omega_f$ in
$\Dctf((X\times_YX)_{\mathrm{proét}},\mathbf Z/\ell^n\mathbf Z)$. Since
$p_2\circ\Delta$ is the identity of $X$, this gives the first isomorphism in

$$
\omega_{f}
\simeq L\Delta^{*}\omega_{p_1}
\xrightarrow{\ \sim\ }z^{*}\omega_{\pi}
\xrightarrow{\ \sim\ }z^{*}(\mathbf Z/\ell^n\mathbf Z)_{T_{X/Y}}(d)[2d]
\simeq(\mathbf Z/\ell^n\mathbf Z)_{X}(d)[2d].
$$

The second isomorphism is the deformation to the normal bundle
[sk-thm-dnc] for the section $\Delta$ of $p_1$, and the third is the inverse
of the vector-bundle purity isomorphism of [sk-prop-an] at the constant
sheaf.

