+++
kind = "proof"
of = "lemma-nearby-duality-proper-direct-image"
order = 1677
uses = ["lemma-internal-adjunction-two-exchange-formulas"]
+++
Under Verdier duality for the proper map $f_\eta$, evaluation on
$Rf_{\eta*}M$ is the composite of the lax monoidal map of $Rf_{\eta*}$,
the map $Rf_{\eta*}\operatorname{ev}_M$, and the
trace $Rf_{\eta*}\omega_{X_\eta}\to\omega_{Y_\eta}$. Hence,
after taking tensor–Hom adjoints, both sides of
(E.13) are the pairing

$$
\begin{split}
Rf_{s*}\Psi_XM\otimes Rf_{s*}\Psi_X\mathbb D M
&\xrightarrow{\chi_f^{-1}\otimes\chi_f^{-1}}
\Psi_YRf_{\eta*}M\otimes \Psi_YRf_{\eta*}\mathbb DM\xrightarrow{\mu_Y}
\Psi_Y(Rf_{\eta*}M\otimes Rf_{\eta*}\mathbb DM)\\
&\longrightarrow \Psi_YRf_{\eta*}(M\otimes \mathbb DM)
\longrightarrow \Psi_YRf_{\eta*}\omega_{X_\eta}
\longrightarrow \Psi_Y\omega_{Y_\eta}
\xrightarrow{\theta_Y}\omega_{Y_s}.
\end{split}
$$

To identify the pairing obtained from $Rf_{s*}\delta_{X,M}$ with this
one, we move the lax monoidal maps past the base change maps for proper
morphisms, and we use the identity
$\theta_X=f_s^!\theta_Y\circ\beta_f(\omega_{Y_\eta})$ of
(E.9).
The lax monoidal maps are compatible with the base change maps because,
after taking ordinary adjoints, both become the tensor
product of the two counits for the open immersions of the generic
fibres. This proves (E.13).

For an open immersion $j$, the map $\alpha_j$ is an isomorphism,
$j^!=j^*$ and $\beta_j=\alpha_j^{-1}$. The argument above therefore
applies with $\alpha_j$ in place of $\chi_f^{-1}$.

For (E.14) we apply
(E.13) to the structure morphism $a$
of $X$. On the trait, $\Psi_S$ takes the stalk at the geometric generic
point, and the pairing (E.12) is
ordinary evaluation. So $\delta_{S,Ra_{\eta*}M}$ is the identity of
$R\operatorname{Hom}_A(R\Gamma(X_{\bar\eta},M),A)$. Global Verdier
duality on both fibres now gives
(E.14).
