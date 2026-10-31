+++
kind = "proof"
of = "sk-prop-sp-orientation"
uses = ["sk-prop-cohsm", "sk-thm-dnc", "sk-prop-an"]
+++
The projection $p_1$ is the base change of $f$ along $f$, so
Proposition [sk-prop-cohsm](3) shows that
$\omega_{p_1}\simeq p_2^{*}\omega_f$. Since $p_2\circ\Delta$ is the
identity of $X$, we get the first isomorphism in

$$
\begin{aligned}
\omega_{f}
&\simeq L\Delta^{*}\omega_{p_1}
\xrightarrow{\sim}z^{*}\omega_{\pi}
\xrightarrow{\sim}z^{*}(\mathbf Z/\ell^n\mathbf Z)_{T_{X/Y}}(d)[2d]
\simeq(\mathbf Z/\ell^n\mathbf Z)_{X}(d)[2d].
\end{aligned}
$$

The second isomorphism is Lemma [sk-thm-dnc] for the section
$\Delta$ of $p_1$, and the third is the inverse of the
isomorphism of Proposition [sk-prop-an]
at the constant sheaf.
