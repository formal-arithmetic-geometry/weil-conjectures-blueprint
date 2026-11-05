+++
id = "example-kummer-no-boundary"
kind = "example"
title = "A Kummer sheaf has no boundary term"
order = 1275
uses = ["lemma-boundary-stalk"]
+++
Let $M$ be the Kummer sheaf of a nontrivial character $\chi$ on
$U_0=\mathbf G_m$. It is irreducible and pure of weight $0$. Since it is tame
at infinity, it has no geometric constituent $\mathcal L_{\psi(ax)}$,
and so it satisfies the hypotheses of this section. Inertia at the
origin acts on $M$ through $\chi$, nontrivially, and hence
$(j_*M)_{\bar0}=0$ by Lemma [lemma-boundary-stalk]. This means that
$j_!M=j_*M$ and $B=0$, and the lemma gives $G\simeq j'_*M'$. On
$\mathbf F_q$-points this is visible: by (16.3) the trace
of $G$ at $y\ne0$ is $-\sum_x\chi(x)\psi(xy)=-\overline\chi(y)g$, with
$g=\sum_x\chi(x)\psi(x)$, and for the quadratic character this is the trace
of $M'$ computed at the start of Chapter [chap-The-Deligne-Laumon-theorem-for-curves].
At $y=0$, on the other hand, the trace of $G$ is $-\sum_x\chi(x)=0$, in agreement with
$H^1_c(\mathbf G_m,M)=0$.
