+++
kind = "proof"
of = "det-sp-dnc-definition"
uses = ["pur9-def-normal-cone"]
+++
The algebra $\mathcal O_X[t,I/t]$ is the extended Rees algebra
$\bigoplus_{r\in\mathbf Z}I^{r}t^{-r}$, with $I^r=\mathcal O_X$ for $r\leq0$. Inverting $t$ gives
$\mathcal O_X[t,t^{-1}]$, so the generic fibre is $X_\eta$. Modulo $t$, the piece of degree $-r$ is
$I^r/I^{r+1}$ for $r\geq0$ and zero for $r<0$, so the fibre over $t=0$ is
$\operatorname{Spec}_Z\bigl(\bigoplus_{r\geq0}I^r/I^{r+1}\bigr)$. The map
$\operatorname{Spec}\mathcal O_S\to\operatorname{Spec}k[t]$ is flat and induces an isomorphism on
residue fields at the closed points, so the base change to $S$ has special fibre $N_ZX$.

Killing $I$ and every $a/t$ leaves $(\mathcal O_X/I)[t]\otimes_{k[t]}\mathcal O_S$, the
coordinate ring of $Z\times S$, so $\widetilde e$ is a closed immersion. Modulo $t$ this quotient
kills the positive-degree part of $\bigoplus_{r\geq0}I^r/I^{r+1}$, which is the zero section of
[pur9-def-normal-cone].
