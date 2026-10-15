+++
id = "pur713-def-coefficient-rings"
kind = "definition"
title = "Pro-étale coefficient rings"
order = 2476
uses = ["pur713-def-continuous-rings", "pur713-def-qbar-ring", "sk-def-sf-setting"]
+++
For a scheme $X$ and $T\in\{\mathcal O_E,E,\overline{\mathbf Q}_\ell\}$, the coefficient ring on $X_{\Proet}$ is the commutative ring object

$$
\mathcal R_{X,T}:=p_X^*\underline T
$$

of $\mathsf{Sh}(X_{\Proet},\mathsf{Ab})$, with $\underline T$ of Definition [pur713-def-continuous-rings] or [pur713-def-qbar-ring] and $p_X^*$ of Input “Pullback from the point” (`pur713-input-point-pullback`, in [sk-def-sf-setting]). In the notation of the governing reference this is $\Lambda_X$ for $\Lambda=\underline T$. Its value on a pro-étale $U$ is not asserted to be $C(|U|,T)$; that description is listed as open in the governing reference, §12, and is not used.
