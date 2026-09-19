+++
id = "lemma-nagata-mem-power-torsion"
kind = "lemma"
title = "Membership in power torsion"
order = 314
lean = ["Submodule.mem_powTorsion_iff"]
uses = ["def-nagata-power-torsion"]
+++
One has

$$
m\in\Gamma_{(a)}(M)
\Longleftrightarrow
\exists n,\ a^nm=0.
$$

The right-hand side should be the simp-normal form for membership.

## Proof

This is the defining membership condition of
[def-nagata-power-torsion]; it should be registered as the simp theorem
for that definition.
