+++
id = "prose-A5-06"
kind = "hidden"
title = "Base change maps for specializing correspondences"
order = 3670
+++
Let $c$ be a correspondence over the trait $S$ and $u$ a cohomological
correspondence on its generic fibre. Applying nearby cycles to $u$ and
composing with base change maps between nearby cycles and the
operations $f^*$, $Rf_*$, $Rf_!$ and $f^!$, we obtain a cohomological
correspondence $u_s$ on the special fibre. We will show in
Proposition [sk-prop-tf-trace-specialization] that the trace of $u_s$ is
the specialization of the trace of $u$. To prove it
we need these base change maps explicitly, together with a few
identities between them.

We can also describe $\nu_f$ on the total families. Write $i_V$ and
$j_V$ for the inclusions $\bar i$ and $\bar j$ of the special and
geometric generic fibres of $V$, so that $\Psi_V=i_V^*Rj_{V*}$. By proper
base change, $i_W^*Rf_!\simeq Rf_{s!}i_V^*$ and
$j_W^*Rf_!\simeq Rf_{\eta!}j_V^*$. Hence the restriction by $i_W^*$ of
the map $Rf_!Rj_{V*}\to Rj_{W*}Rf_{\eta!}$ whose $j_W^*$-adjoint is

$$
j_W^*Rf_!Rj_{V*}\simeq Rf_{\eta!}j_V^*Rj_{V*}
                  \xrightarrow{Rf_{\eta!}\varepsilon_{j_V}}Rf_{\eta!}
$$

is a map $Rf_{s!}\Psi_V\to \Psi_WRf_{\eta!}$, and we claim that it is
$\nu_f$. Both constructions are compatible with composition, so it
suffices to check this for $p$ and for $h$. For proper $p$ the
restricted map is $\chi_p^{-1}$, by proper base change for $i_W^*$.
For the open immersion $h$ we have $h_\eta^*h_{\eta!}=1$, and the
$h_s^*$-adjoint of the restricted map is $\alpha_h^{-1}$, as in the
definition of $\nu_h$.

In the proof of Proposition [sk-prop-tf-trace-specialization] we move the
base change maps past the projection formula, composition, external
duality and the cartesian square defining the fixed point scheme.  The following lemma collects the
identities we need.
