+++
kind  = "proof"
of    = "def-sfb-modobj-extend-restrict-adjunction"
+++
Write $p\colon\mathcal S\otimes M\to\mathcal S\otimes_{\mathcal R}M$ for the projection
([def-sfb-modobj-extension]). Up to unitors, the coequalizer relation gives
$$
u_M\gamma_M=p(\mathcal S\otimes\gamma_M)(\eta_{\mathcal S}\otimes\mathcal R\otimes M)
=p\bigl(\mu_{\mathcal S}(\eta_{\mathcal S}\otimes\varphi)\otimes M\bigr)=p(\varphi\otimes M).
$$
The restricted action of $\mathcal R$ on $\mathcal S\otimes_{\mathcal R}M$, applied after
$\mathcal R\otimes u_M$, gives
$p(\mu_{\mathcal S}\otimes M)(\varphi\otimes\eta_{\mathcal S}\otimes M)=p(\varphi\otimes M)$
as well. So $u_M$ is $\mathcal R$-linear.

Conversely, let $f\colon M\to\operatorname{Res}_\varphi N$ be $\mathcal R$-linear. Then
$\gamma_N(\mathcal S\otimes f)\colon\mathcal S\otimes M\to N$ coequalizes the two parallel
maps, because $f$ is linear for the action through $\varphi$ and $\gamma_N$ is associative.
It therefore descends to a map $\mathcal S\otimes_{\mathcal R}M\to N$, which is
$\mathcal S$-linear. The two constructions are mutually inverse:
- by the unit law, $\gamma_N(\mathcal S\otimes f)(\eta_{\mathcal S}\otimes M)=f$;
- an $\mathcal S$-linear $g$ is determined by $gp$, and by $\mathcal S$-linearity
  $gp=\gamma_N(\mathcal S\otimes gu_M)$.

Naturality in $M$ and $N$ is immediate.
