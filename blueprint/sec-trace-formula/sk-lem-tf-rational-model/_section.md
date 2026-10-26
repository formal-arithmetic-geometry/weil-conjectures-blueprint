+++
id = "sk-lem-tf-rational-model"
kind = "lemma"
title = "Integral models for rational Frobenius correspondences"
order = 3527
uses = ["sk-d-weil", "sk-thm-sfb-rationalization-comparison", "sk-lem-integral-models"]
tags = ["sketch"]
+++
Let $X_0/\mathbf F_q$ be separated and of finite type, $X=X_0\times_{\mathbf F_q}k$,
and $E/\Ql$ finite with uniformizer $\pi_E$.

Let $K_E\in\Dbc(X,E)$ and let
$\psi_E:\Phi_X^*K_E\to K_E$ be any morphism in $\Dbc(X,E)$. There
exist $K_0\in\Dbc(X,\mathcal O_E)$, an isomorphism
$K_0\dt_{\mathcal O_E}E\simeq K_E$, an integer $N\geq0$, and a
Frobenius correspondence $\theta:\Phi_X^*K_0\to K_0$ such that

$$
 \psi_E=\pi_E^{-N}(\theta\dt_{\mathcal O_E}E).
$$

For every $m\geq1$ the operators of [sk-d-weil]
satisfy

$$
 \begin{aligned}
 T_{c_m}((\psi_E)_m)&=\pi_E^{-Nm}
     \bigl(T_{c_m}(\theta_m)\dt_{\mathcal O_E}E\bigr),\\
 (\psi_E)_{m,\bar y}&=\pi_E^{-Nm}
     \bigl(\theta_{m,\bar y}\dt_{\mathcal O_E}E\bigr).
 \end{aligned}
 \tag{1}
$$
