+++
kind = "proof"
of = "lemma-compatibilities-base-change-maps"
order = 1654
+++
The identity follows, after taking $Rf_{s!}$-adjoints, from the
compatibility of $\nu_f$ with the projection formula: for $L$ on $V_\eta$ and $N$ on $W_\eta$,
the composite

$$
Rf_{s!}(\Psi_VL\otimes^{\mathbf L} f_s^*\Psi_WN)\xrightarrow{\mu_V(1\otimes\alpha_f)}
Rf_{s!}\Psi_V(L\otimes^{\mathbf L} f_\eta^*N)\xrightarrow{\nu_f}
\Psi_WRf_{\eta!}(L\otimes^{\mathbf L} f_\eta^*N)\simeq \Psi_W(Rf_{\eta!}L\otimes^{\mathbf L} N)
$$

equals the projection formula on the special fibre followed by
$\mu_W(\nu_f\otimes1)$. To check this, we use the description of
$\nu_f$ on the total families and compare $j_W^*$-adjoints. On both
sides the adjoint is the counit $j_V^*Rj_{V*}\to1$ tensored with the
identity, followed by the projection formula on the generic fibre.

Taking $Rf_{s!}$-adjoints in
(E.8) and applying the projection
formula, the left side becomes the following composite by this
compatibility, and the right side becomes it by naturality
of $\mu_W$:

$$
\begin{split}
Rf_{s!}\Psi_Vf_\eta^!M\otimes^{\mathbf L} \Psi_WN
&\xrightarrow{\nu_f\otimes1}
\Psi_W(Rf_{\eta!}f_\eta^!M)\otimes^{\mathbf L} \Psi_WN\\
&\xrightarrow{\mu_W}\Psi_W(Rf_{\eta!}f_\eta^!M\otimes^{\mathbf L} N)
\xrightarrow{\Psi_W(\varepsilon_{f_\eta}\otimes1)}\Psi_W(M\otimes^{\mathbf L} N).
\end{split}
$$

Since the adjoints agree, so do the maps.
