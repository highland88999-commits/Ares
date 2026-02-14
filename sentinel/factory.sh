#!/bin/bash
# Ares Factory: Plants realistic traps based on the 'Terrain'

TERRAIN=$1 # 'wordpress', 'node', or 'python'

case $TERRAIN in
  "wordpress")
    touch wp-config-backup.php
    echo "<?php // Ares Trap: SQL_PASS='trap_pass' ?>" > wp-config-backup.php
    ;;
  "node")
    touch .env.production
    echo "STRIPE_KEY=sk_test_ares_trap_123" > .env.production
    ;;
esac

echo "Ares: Terrain-specific honey-tokens planted for $TERRAIN."
