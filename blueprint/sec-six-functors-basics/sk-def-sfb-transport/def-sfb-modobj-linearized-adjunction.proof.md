+++
kind  = "proof"
of    = "def-sfb-modobj-linearized-adjunction"
+++
Let $\varphi\colon PM\to N$ have adjoint $\varphi^\flat\colon M\to GN$, so that
$\varphi=c_N\circ P\varphi^\flat$. By [def-sfb-modobj-linearization], $\varphi$ is
$\mathcal B$-linear if and only if
$$
\varphi\circ P\gamma_M=\gamma_N(\mathcal B\otimes\varphi)\pi_{\mathcal B,M}.
$$
Naturality of $\pi$ in $M$ gives
$(\mathcal B\otimes\varphi)\pi_{\mathcal B,M}
=(\mathcal B\otimes c_N)\pi_{\mathcal B,GN}P(S\mathcal B\otimes\varphi^\flat)$. So the
adjoint of the right side is
$G(\gamma_N)\theta_{\mathcal B,N}(S\mathcal B\otimes\varphi^\flat)$. The adjoint of the left
side is $\varphi^\flat\gamma_M$. Hence $\varphi$ is $\mathcal B$-linear if and only if
$\varphi^\flat$ is $S\mathcal B$-linear for the action of
[def-sfb-modobj-linearization-right-adjoint]. Naturality is inherited from $P\dashv G$.
