<?php

namespace App\Tests\Controller;

use Symfony\Bundle\FrameworkBundle\KernelBrowser;

/**
 * Controller test helper
 */
class Helper
{
    /**
     * Get client response array
     *
     * @param KernelBrowser $client
     * @return array
     */
    public static function getResponceArray(KernelBrowser $client): array
    {
        $client_content = $client->getResponse()->getContent();
        $response_array = json_decode($client_content, true);

        return $response_array;
    }
}
