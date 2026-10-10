+++
kind  = "proof"
of    = "cor-wf-rank-one-degree-factorization-curve"
+++
The degree homomorphism $\deg:W(U_0,\bar u)\to\mathbf Z$ of
[def-wf-weil-group] is surjective with kernel $\Pi$ by
[lem-wf-weil-group-exact-sequence], and $\deg(s)=1$, so
$(W(U_0,\bar u),\deg,s)$ is a degree datum of [d-monodromy] with
$P=\Pi$. In the notation of [d-ab-rankone], $z=\chi(s)=c$,
$\chi_z(w)=c^{\deg(w)}$ and $\varepsilon=\chi_{\mathrm{fin}}$.
Since $\deg$ is additive, $\chi_z$ is a character, and since
$E^\times$ is abelian, the quotient $\varepsilon=\chi\chi_z^{-1}$ is again a
character. If $n=\deg(w)$, then $g=ws^{-n}$ has degree zero and hence
lies in $\Pi$; multiplicativity gives

$$
\varepsilon(w)=\chi(g)\chi(s)^nc^{-n}=\chi(g)\in\chi(\Pi),
$$

and conversely $\varepsilon(g)=\chi(g)$ for $g\in\Pi$, so
$\varepsilon(W(U_0,\bar u))=\chi(\Pi)$, and $\varepsilon(s)=\chi(s)c^{-1}=1$.
The group $\chi(\Pi)$ is finite by hypothesis. Thus the image of
$\varepsilon$ is finite, so $\varepsilon$ is of finite order, and the
displayed factorization $\chi=\varepsilon\chi_z$ holds by the definition of
$\chi_{\mathrm{fin}}$ in [d-ab-rankone].
