+++
kind = "proof"
of = "det-tf-nearby-duality-proper"
+++
*(1)* Under proper Verdier duality, evaluation on $Rf_{\eta*}M$ is the composite of the
lax product of $Rf_{\eta*}$, $Rf_{\eta*}\operatorname{ev}_M$, and the trace
$Rf_{\eta*}\omega_{X_\eta}\to\omega_{Y_\eta}$. Thus, after taking tensor–Hom adjoints,
$\delta_{Y,Rf_{\eta*}M}$ corresponds to the pairing

$$
\begin{aligned}
 Rf_{s*}S_XM\otimes Rf_{s*}S_X\mathbb D M
 &\xrightarrow{\chi_f^{-1}\otimes\chi_f^{-1}}
 S_YRf_{\eta*}M\otimes S_YRf_{\eta*}\mathbb DM\xrightarrow{\mu_Y}
 S_Y(Rf_{\eta*}M\otimes Rf_{\eta*}\mathbb DM)\\
 &\longrightarrow S_YRf_{\eta*}(M\otimes \mathbb DM)
 \longrightarrow S_YRf_{\eta*}\omega_{X_\eta}
 \longrightarrow S_Y\omega_{Y_\eta}
 \xrightarrow{\theta_Y}\omega_{Y_s}.
\end{aligned}
$$

The pairing obtained from $Rf_{s*}\delta_{X,M}$ is the lax product of $Rf_{s*}$
followed by $Rf_{s*}$ of the pairing defining $\delta_{X,M}$ and the trace
$Rf_{s*}\omega_{X_s}\to\omega_{Y_s}$. Two identities convert it into the pairing above.
First, the lax products commute through proper exchange: taking ordinary adjoints,
both maps become the tensor product of the two generic-open counits
$j^*Rj_*\to1$. Second,

$$
 \theta_X=f_s^!\theta_Y\circ\beta_f(\omega_{Y_\eta}),
$$

which follows by taking exceptional adjoints: $\beta_f$ is the exceptional adjoint of
$S_Y(\varepsilon_{f_\eta})\circ\nu_f$, with $\nu_f=\chi_f^{-1}$, and the counits of
$a_Y$ and $f$ compose to the counit of $a_X=a_Yf$. Substituting both identities proves (1).

*(2)* For an open immersion the nearby smooth exchange $\alpha_j$ is an isomorphism,
$j^!=j^*$ on both fibres, and $\beta_j=\alpha_j^{-1}$. The lax tensor map is
compatible with $\alpha_j$ (monoidality), and $\theta_U=j_s^*\theta_X\circ\beta_j$ by
the composition law for $\beta$. Hence the pairing defining $\delta_{X,M}$ restricts to
the pairing defining $\delta_{U,j_\eta^*M}$.

*(3)* Apply (1) to the structure map $a:X\to S$. Nearby cycles on the trait itself
are the underlying geometric-generic complex, $S_S(N)=N_{\bar\eta}$, and with
$\theta_S$ the identity of $A$ the normalized pairing on $S$ is ordinary evaluation
$N_{\bar\eta}\otimes R\operatorname{Hom}_A(N_{\bar\eta},A)\to A$. So $\delta_{S,N}$ is
the identity of $R\operatorname{Hom}_A(N_{\bar\eta},A)$. With
$N=Ra_{\eta*}M$ and $(Ra_{\eta*}M)_{\bar\eta}=R\Gamma(X_{\bar\eta},M)$ by proper base
change, (1) identifies $R\Gamma(X_s,\delta_{X,M})=Ra_{s*}\delta_{X,M}$ with this
identity.
