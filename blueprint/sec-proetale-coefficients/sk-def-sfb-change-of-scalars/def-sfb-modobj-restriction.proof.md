+++
kind  = "proof"
of    = "def-sfb-modobj-restriction"
+++
Unit law: $\gamma_N(\varphi\otimes N)(\eta_{\mathcal R}\otimes N)
=\gamma_N(\eta_{\mathcal S}\otimes N)=\lambda_N$, since $\varphi\eta_{\mathcal R}=\eta_{\mathcal S}$.

Associativity: since $\varphi\mu_{\mathcal R}=\mu_{\mathcal S}(\varphi\otimes\varphi)$,
$$
\gamma_N(\varphi\otimes N)(\mu_{\mathcal R}\otimes N)
=\gamma_N(\mu_{\mathcal S}\otimes N)((\varphi\otimes\varphi)\otimes N)
=\gamma_N(\mathcal S\otimes\gamma_N)\alpha((\varphi\otimes\varphi)\otimes N).
$$
By naturality of $\alpha$ and the interchange law, this is
$\gamma_N(\varphi\otimes N)\bigl(\mathcal R\otimes\gamma_N(\varphi\otimes N)\bigr)\alpha$.

Linearity: for $\mathcal S$-linear $f\colon N\to N'$,
$f\gamma_N(\varphi\otimes N)=\gamma_{N'}(\mathcal S\otimes f)(\varphi\otimes N)
=\gamma_{N'}(\varphi\otimes N')(\mathcal R\otimes f)$.
