+++
id = "lem-trf-integration-as-pushforward"
kind = "lemma"
title = "Integration is pushforward to the point"
order = 3711
uses = ["def-trf-borel-moore-pushforward", "def-trf-dualizing-complex", "def-trf-integration", "thm-trf-dualizing-complex-composition"]
+++
Fix the global finite-field datum
and the coefficient
conventions, $A=A_{E,n}$, $s=\Spec k$, and let $T$ be
separated finite type
and proper over $s$
with exceptionally admissible
structure morphism $a_T:T\to s$. Identify
$\omega_s=Ra_s^!A_s=A_s$ ($a_s=\operatorname{id}_s$) and
$\End_{D(s,A)}(A_s)=\End_{D(A)}(A)=A$ via $R\Gamma(s,-)$. Then for
every Borel–Moore section $\alpha:A_T\to\omega_T$ of
[def-trf-borel-moore-pushforward],

$$
\int_T\alpha=(a_T)_*\alpha\in A,
$$

where $\int_T$ is the integration of [def-trf-integration] and
$(a_T)_*$ the pushforward of [def-trf-borel-moore-pushforward]
along the proper morphism $h=a_T:T\to T'=s$.
