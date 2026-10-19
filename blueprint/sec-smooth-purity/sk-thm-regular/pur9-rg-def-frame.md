+++
id = "pur9-rg-def-frame"
kind = "definition"
title = "Frames and frame classes"
order = 2375
uses = ["pur9-rg-def-supported"]
+++
A frame of $Z\subset X$ is an étale morphism $U\to X$ together with $f_1,\dots,f_c\in\Gamma(U,\mathcal O_U)$ generating the ideal of $Z_U=Z\times_XU$. Each $f_r$ is a unit on $U\setminus V(f_r)$, with Kummer class $\kappa(f_r)\in H^1((U\setminus V(f_r))_{\Et},(\mathcal O_E/\pi_E^n)(1))$. The class of the frame is

$$
\operatorname{cl}(f):=\partial\kappa(f_1)\cup\cdots\cup\partial\kappa(f_c)\in H^{2c}_{Z_U}(U_{\Et},(\mathcal O_E/\pi_E^n)(c)),
$$

with $\partial$ and the cup product with supports of Definition [pur9-rg-def-supported].
