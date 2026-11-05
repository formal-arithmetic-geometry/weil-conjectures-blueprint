+++
id = "definition-frobenius-operator"
kind = "definition"
title = "Frobenius operator"
order = 877
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.WeilBoundedConstructible.compactFrobenius", "AlgebraicGeometry.ProEtale.CondensedRing.WeilBoundedConstructible.compactFrobenius_eq"]
uses = ["definition-weil-structure", "proposition-construction-independence-rf-shriek", "proposition-six-operations-dctf", "proposition-forgetting-supports-composition", "proposition-composition-base-change-rf-shriek", "lemma-comparison-via-relative-frobenius--1"]
+++
For a Weil complex $(K,\phi_K)$ on $T$, the *geometric Frobenius
operator* on compactly supported cohomology is the endomorphism

$$
\begin{gathered}
\operatorname{Frob}_{T,K}:R\Gamma_c(T_{\mathrm{pro}\acute{e}t},K)
\xrightarrow{\ \text{pullback along }\operatorname{Fr}_T\ }
R\Gamma_c(T_{\mathrm{pro}\acute{e}t},\operatorname{Fr}_T^*K)\\
\xrightarrow{\ R\Gamma_c(T_{\mathrm{pro}\acute{e}t},\phi_K)\ }
R\Gamma_c(T_{\mathrm{pro}\acute{e}t},K).
\end{gathered}
$$

Here pullback along $\operatorname{Fr}_T$ is the composite

$$
R\Gamma_c(T_{\mathrm{pro}\acute{e}t},K)\xrightarrow{\ R\Gamma_c(T_{\mathrm{pro}\acute{e}t},\eta)\ }R\Gamma_c(T_{\mathrm{pro}\acute{e}t},R\operatorname{Fr}_{T*}\operatorname{Fr}_T^*K)\simeq R\Gamma\bigl(s,R\gamma_{s!}Ra_{T!}\operatorname{Fr}_T^*K\bigr)\xrightarrow{\ \lambda_\gamma\ }R\Gamma_c(T_{\mathrm{pro}\acute{e}t},\operatorname{Fr}_T^*K),
$$

where $s=\operatorname{Spec}k$, $a_T:T\to s$ is the structure map, $\gamma_s=\operatorname{Spec}(\sigma)$ is the automorphism of $s$ covered by $\operatorname{Fr}_T$, so that $a_T\circ\operatorname{Fr}_T=\gamma_s\circ a_T$, $\eta:K\to R\operatorname{Fr}_{T*}\operatorname{Fr}_T^*K$ is the unit, the middle identification uses $R\operatorname{Fr}_{T*}=R\operatorname{Fr}_{T!}$ and the composition isomorphism for $Ra_{T!}R\operatorname{Fr}_{T!}=R\gamma_{s!}Ra_{T!}$, and $\lambda_\gamma:R\Gamma(s,R\gamma_{s!}(-))\xrightarrow{\sim}R\Gamma(s,-)$ is the canonical identification of sections along the base automorphism $\gamma_s$, which is compatible with identities and composition. The operator on ordinary cohomology is defined in the same way with $Ra_{T*}$, $R\operatorname{Fr}_{T*}$ and the corresponding identification for $R\gamma_{s*}$.
