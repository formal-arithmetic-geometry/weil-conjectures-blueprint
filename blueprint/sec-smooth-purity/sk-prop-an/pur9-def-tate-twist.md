+++
id = "pur9-def-tate-twist"
kind = "definition"
title = "Tate twists"
order = 2879
uses = ["pur9-def-twist-module"]
+++
Let $W$ be a $k$-scheme and $\tau\in\{\Et,\Proet\}$. For $m\in\mathbf Z$, $(\mathcal O_E/\pi_E^n)_W(m)$ is the constant sheaf on $W_\tau$ with value $P(m)$ of Definition [pur9-def-twist-module], i.e. the sheafification of the constant presheaf, an object of $\mathsf{Sh}(W_\tau,\mathsf{Mod}_{\mathcal O_E/\pi_E^n})$. For $K\in D(W_\tau,\mathcal O_E/\pi_E^n)$ the *twist* is

$$
K(m):=K\otimes^L_{\mathcal O_E/\pi_E^n}(\mathcal O_E/\pi_E^n)_W(m),
$$

with the derived tensor product of Definition “Finite-coefficient derived tensor product” (`pur713-def-tensor`) and the twist sheaf in degree zero. The site is always the one of $K$.
