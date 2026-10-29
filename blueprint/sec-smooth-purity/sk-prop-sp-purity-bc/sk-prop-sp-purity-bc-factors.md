+++
id = "det-sp-purity-bc-factors"
kind = "lemma"
title = "Base change of the orientation and of the tensor map"
order = 3370
uses = ["det-sp-tower-exceptional-bc", "det-sp-tower-gamma", "det-sp-orientation-charts", "thm-pur-diagonal-dualizing-object"]
+++
In a Cartesian square as in the sketch, with coefficients a finite ring $A$ or
the towers $\mathcal O_E/\ell^\bullet$ (write $\bullet$ for either; for finite $A$ drop
the index):

1. *Orientation.* Under $u^*_\bullet\omega_{f,\bullet}\simeq\omega_{f',\bullet}$ (the
   exceptional base change at the unit object) and
   $u^*_\bullet(\mathcal O_X/\ell^\bullet)(d)[2d]=(\mathcal O_{X'}/\ell^\bullet)(d)[2d]$, the
   pullback of the orientation of $f$ is the orientation of $f'$;
2. *Tensor map.* For $K_\bullet$ on $Y$, under $e_{f,\bullet}$ and
   $u^*_\bullet f^*_\bullet\simeq f'^*_\bullet v^*_\bullet$, the pullback of the tensor map
   $f^*_\bullet K_\bullet\otimes\omega_{f,\bullet}\to f^!_\bullet K_\bullet$ is the tensor map
   for $f'$ at $v^*_\bullet K_\bullet$.

Consequently $u^*_\bullet\gamma_{f,\bullet}(K_\bullet)=\gamma_{f',\bullet}(v^*_\bullet K_\bullet)$.
