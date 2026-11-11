+++
id = "lemma-integral-models-rational-frobenius-correspondences"
kind = "lemma"
title = "Integral models for rational Frobenius correspondences"
order = 1014
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.exists_integralModel_frobeniusCorrespondence", "AlgebraicGeometry.ProEtale.CondensedRing.pow_smul_upperStar_map_frobeniusCoefficientIterate_eq"]
uses = ["lemma-stability", "definition-constructible-sheaves", "definition-lisse-sheaves", "definition-change-of-coefficients-maps"]
+++
Let $K_E\in\Dbc(X,E)$ and let
$\psi_E:\Phi_X^*K_E\to K_E$ be any morphism. There
exist $K_0\in\Dbc(X,\mathcal O_E)$, an isomorphism
$K_0\otimes^{\mathbf L}_{\mathcal O_E}E\simeq K_E$, an integer $N\geq0$, and a
Frobenius correspondence $\theta:\Phi_X^*K_0\to K_0$ such that

$$
\psi_E=\pi_E^{-N}(\theta\otimes^{\mathbf L}_{\mathcal O_E}E).
$$

For every $m\geq1$ the operators of Definition [definition-frobenius-correspondences-their-operators]
satisfy

$$
\begin{aligned}
T_{c_m}((\psi_E)_m)&=\pi_E^{-Nm}
\bigl(T_{c_m}(\theta_m)\otimes^{\mathbf L}_{\mathcal O_E}E\bigr),\\
(\psi_E)_{m,\bar y}&=\pi_E^{-Nm}
\bigl(\theta_{m,\bar y}\otimes^{\mathbf L}_{\mathcal O_E}E\bigr).
\end{aligned}
\tag{12.2}
$$
